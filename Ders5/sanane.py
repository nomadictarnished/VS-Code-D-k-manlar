import requests

def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        data = response.json()  # If the data is in JSON format
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage
url_to_data_source = "https://dog.ceo/api/breeds/image/random"
data_from_source = fetch_data_from_url(url_to_data_source)

if data_from_source:
    # Process the data here
    print(data_from_source)