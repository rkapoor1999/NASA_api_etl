import requests
import csv

api_key = 'hzjb5me6c39Eo1ezJUyLr13cUB4kfVY0hFpP5usm'

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
        csv_filename = 'data/NASA_data.csv'

        try:
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=apod_data.keys())
                writer.writeheader()
                writer.writerow(apod_data)
        except Exception as E:
            print(E)
    else:
        print("Failed to fetch APOD data.")

if __name__ == '__main__':
    main()