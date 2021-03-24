import pandas as pd
from urllib.error import HTTPError
from urllib.request import urlretrieve

listings = pd.read_csv('data/nyc-listings.csv')  # testing data
# listings = pd.read_csv('data/listings.csv')
listings.info()
count = 0  # count for successful downloads
err_count = 0  # error counts
for index, row in listings.iterrows():
    # print(row["id"], row["xl_picture_url"])
    # check whether the URL exists
    if pd.isnull(row["xl_picture_url"]):
        url = row["picture_url"]
    else:
        url = row["xl_picture_url"]

    try:
        urlretrieve(url, "./data/images/" + str(row["id"]) + ".jpg")
        count += 1
        print("downloading " + str(row["id"]))
    except FileNotFoundError as err:
        print(err)  # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url
    except:
        print("something is wrong, skipped one line")


print("downloading complete with " + str(count) + " images.")