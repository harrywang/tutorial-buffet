from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import csv
import os
import pandas as pd
from urllib.error import HTTPError
from urllib.request import urlretrieve

# you need to change the following parameters

listing_file = 'data/nyc-listings_new.csv'
csv_file = 'data/listing_photos.csv'

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# setup ProxyMesh service
# make sure you add the IP of the machine running this script to you ProxyMesh account for IP authentication

PROXY = "us-wa.proxymesh.com:31280" # IP:PORT or HOST:PORT you get this in your account once you pay for a plan
chrome_options.add_argument('--proxy-server=%s' % PROXY)

# for Mac, install Chrome and Chrome driver: `brew install chromedriver`
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver")

# for Linux use the following approach
# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
# chrome_driver = os.getcwd() +"\\chromedriver.exe"
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

print("start loading listing file...")
listings = pd.read_csv(listing_file)  # testing data
# listings = pd.read_csv('data/listings.csv')
# listings.info()


total_listings = 0  # total listings with successful photo downloads
total_photo_download = 0  # count for successful photo downloads
err_count = 0  # error counts
csv_columns = ['listing_id', 'seq', 'caption', 'url']
# currentPath = os.getcwd()
#


# function to write dictionary to csv, append with 'a' not overwrite with 'w'
# header is required
# 'listing_id', 'seq', 'caption', 'url'
def write_dict_to_csv(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            file_empty = os.stat(csv_file).st_size == 0
            if file_empty:
                writer.writeheader()  # file doesn't exist yet, write a header
            for data in dict_data:
                writer.writerow(data)
    except IOError as err:
            print(err)
    return


# function to download all photos to a folder
def save_photos(photo):
    folder_name = "./data/images/" + str(photo['listing_id']) + "/"
    file_name = str(photo['listing_id']) + "-" + str(photo['seq']) + ".jpg"

    # create the folder if not exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        urlretrieve(photo['url'], folder_name + file_name)
        print("downloading " + file_name)
    except FileNotFoundError as err:
        print(err)  # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url
    except:
        print("something is wrong when downloading photo, skipped one line: ", photo['url'])
    return


# function to download host photo to a folder
def save_host_photo(listing_id, host_pic_url):
    folder_name = "./data/images/" + str(listing_id) + "/"
    file_name = str(listing_id) + "-" + "host" + ".jpg"

    # create the folder if not exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        urlretrieve(host_pic_url, folder_name + file_name)
        print("downloading host picture " + file_name)
    except FileNotFoundError as err:
        print(err)  # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url
    except:
        print("something is wrong when downloading host photo, skipped one line: ")
    return


# loop through the listings
for index, row in listings.iterrows():
    print("processing listing: ", row["id"])

    if pd.isnull(row["listing_url"]):
        err_count += 1
        print("no listing url: ", row["id"])
        continue
    else:
        # get host photo
        if row["host_photo_downloaded"] == "f":
            print(row["id"], row["host_picture_url"])
            save_host_photo(row["id"], row["host_picture_url"])
            listings.at[index, 'host_photo_downloaded'] = "t"
        else:
            print("listing host photo already downloaded: ", row["id"])

        # get listing photos
        if row["photo_downloaded"] == "f":
            try:  # if anything goes wrong, just skip to the next one
                driver.get(row["listing_url"])
                total_listings += 1
                time.sleep(1)
                # find the view photo button and click it, go to next one if not found
                view_photo_button = driver.find_element_by_css_selector("button[data-veloute='hero-view-photos-button']")
                view_photo_button.click()  # click the view photo button
                print("Clicking View Photo button for listing: ", row["id"])
                time.sleep(1)

                new_photo = True  # flag to see whether we loop through all photos or not
                total_photo = 1  # total photos per listing, assume at least one photo
                photos = []
                photo = {}
                photo['listing_id'] = row["id"]

                while new_photo:
                    try:
                        # get the current shown photo
                        current_image = driver.find_element_by_css_selector("ul.Slideshow__images img")
                        url = current_image.get_attribute("src")
                        caption = current_image.get_attribute("alt")
                        # caption = driver.find_element_by_css_selector("figcaption span").text
                        print("Processing photo:", total_photo, caption, url)
                        photo['seq'] = total_photo
                        photo['caption'] = caption
                        photo['url'] = url

                        photos.append(photo.copy())

                        # download and save photo
                        save_photos(photo)
                        print("photo " + str(total_photo) + " saved.")

                        # click next button
                        next_button = driver.find_element_by_css_selector("button[aria-label='Next']")
                        next_button.click()
                        # print("clicking next")
                        time.sleep(1)
                        current_image = driver.find_element_by_css_selector("ul.Slideshow__images img")
                        url = current_image.get_attribute("src")
                        caption = current_image.get_attribute("alt")
                        total_photo += 1

                        # check whether the current image is new or not
                        for p in photos:
                            if p['url'] == url:
                                new_photo = False

                        if not new_photo:
                            break
                    except:
                        print("something wrong with individual photo, move on to the next one.")

                total_photo -=1
                total_photo_download += total_photo
                print(total_photo, " photos downloaded. for listing: ", row["id"])

                # update the listings dataframe
                listings.at[index, 'photo_downloaded'] = "t"
                listings.at[index, 'total_photos'] = total_photo

                # write the listing photos information to csv
                write_dict_to_csv(csv_file, csv_columns, photos)

            except:
                print("something went wrong for the listing, skip to the next listing: ", row["id"])
                continue
        else:
            print("listing photos already downloaded: ", row["id"])

print("Total listings: ", total_listings, " with ", total_photo_download, " photos downloaded")

# write the new listings info to csv
listings.to_csv(listing_file, encoding='utf-8', index=False)

driver.close()  # close chrome


# capture the screen
# driver.get_screenshot_as_file("capture.png")
