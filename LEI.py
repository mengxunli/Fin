import requests
import json

# Define the URL
url = 'https://api.gleif.org/api/v1/lei-records/02Q37D0NZ4LRWNCY0996'

# Perform the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the required fields
    record_id = data['data']['id']
    legal_name = data['data']['attributes']['entity']['legalName']['name']
    jurisdiction = data['data']['attributes']['entity']['jurisdiction']
    legal_address_country = data['data']['attributes']['entity']['legalAddress']['country']

    # Create a dictionary with the extracted fields
    extracted_data = {
        'id': record_id,
        'legal_name': legal_name,
        'jurisdiction': jurisdiction,
        'legal_address_country': legal_address_country
    }

    # Store the extracted data in a JSON file
    with open('extracted_lei_record.json', 'a') as f:
        json.dump(extracted_data, f, indent=4)

    print("Data successfully saved to extracted_lei_record.json")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
