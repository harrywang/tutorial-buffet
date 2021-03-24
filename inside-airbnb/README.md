# About

Code to download the images by using the image URLs provided in the NYC data from
http://insideairbnb.com/get-the-data.html and save those images into local folders.

# Setup and Run

Python 3

- create virtual environment: `$virtualenv -p python3 venv`
- activate virtual env: `$source venv/bin/activate`
- install required packages: `pip3 install -r requirements.txt`

To run (NOTE: for the NYC dataset, it took about 4.5 hours to download the ~ 45,000 images):

1. copy the real listing csv file to /data/ and comment out the `# listings = pd.read_csv('data/listings.csv')`
2. `python3 get-images.py` will download the save the images to /data/images/ folder



Use Katalon Recorder (Selenium IDE for Chrome) to help test the css selector:

Install at: https://chrome.google.com/webstore/detail/katalon-recorder-selenium/

Then enter the css selector as below and search to see whether you are find the element you need:

<img width="736" alt="screen shot 2018-02-14 at 1 32 32 pm" src="https://user-images.githubusercontent.com/595772/36221494-3cf3391e-118c-11e8-891c-716b8a7fcf3c.png">

Example: open https://www.airbnb.com/rooms/18461891 in chrome and search css=button[data-veloute='hero-view-photos-button'], the View Photo button should be highlighted