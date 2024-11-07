import sys
from opencage.geocoder import OpenCageGeocode
import pandas as pd

# API key for OpenCage Geocode
import os
from dotenv import load_dotenv
load_dotenv(".env")
API_KEY= os.getenv("API_KEY")
geocoder = OpenCageGeocode(API_KEY)

# Load the CSV file
df = pd.read_csv('EKITI_crosschecked - EKITI_crosschecked.csv')

# Initialize lists to store the results
longitudes = []
latitudes = []

try:
    for address in df['Address']:
        # Geocode the address
        results = geocoder.geocode(address, no_annotations='1')

        if results and len(results):
            longitude = results[0]['geometry']['lng']
            latitude = results[0]['geometry']['lat']
            longitudes.append(longitude)
            latitudes.append(latitude)
            print(f'{latitude};{longitude};{address}')
        else:
            longitudes.append(None)
            latitudes.append(None)
            sys.stderr.write(f"not found: {address}\n")
except IOError:
    print(f'Error: File does not appear to exist.')
    # Your rate limit has expired. It will reset to 2500 at midnight UTC timezone
    # Upgrade on https://opencagedata.com/pricing

# Add the longitude and latitude to the dataframe
df['Longitude'] = longitudes
df['Latitude'] = latitudes

# Save the updated dataframe to a new CSV file
output_file_path = 'EKITI_geocoded.csv'
df.to_csv(output_file_path, index=False)

output_file_path

