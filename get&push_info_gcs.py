import requests
import csv
from google.cloud import storage
import os

os.environ["GCLOUD_PROJECT"] = "NASA Project"
api_key = 'hzjb5me6c39Eo1ezJUyLr13cUB4kfVY0hFpP5usm'
csv_filename = 'data/NASA_data.csv'
csv_filename_gcs = 'apod_data.csv'

def fetch_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data from the API")
        return None
    
def main():
    apod_data = fetch_apod(api_key)
    if apod_data:
        try:
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=apod_data.keys())
                writer.writeheader()
                writer.writerow(apod_data)
        except Exception as E:
            print(E)
    else:
        print("Failed to fetch APOD data.")

def gcs_upload():
    # Upload the CSV file to GCS
    bucket_name = 'nasa_apod_data'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f'{csv_filename_gcs}'  # The path to store in GCS

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(csv_filename)

    print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

if __name__ == '__main__':
    main()
    gcs_upload()