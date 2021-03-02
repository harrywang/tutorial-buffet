import pandas as pd

listings = pd.read_csv('data/nyc-listings.csv')  # testing data
# listings = pd.read_csv('data/listings.csv')
listings.info()

listings["total_photos"] = 0

# the original list used string not boolean
listings["photo_downloaded"] = "f"
listings["host_photo_downloaded"] = "f"

listings.to_csv('data/nyc-listings_new.csv', encoding='utf-8', index=False)

print("csv file processed")