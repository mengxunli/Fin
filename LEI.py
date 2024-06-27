# import requests
# import json

# # Define the URL
# #url = 'https://api.gleif.org/api/v1/lei-records/02Q37D0NZ4LRWNCY0996'


# # Check if the request was successful
# def get_LEI(LID):
#     url = 'https://api.gleif.org/api/v1/lei-records/' + str(LID)
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()

#         # Extract the required fields
#         record_id = data['data']['id']
#         legal_name = data['data']['attributes']['entity']['legalName']['name']
#         jurisdiction = data['data']['attributes']['entity']['jurisdiction']
#         legal_address_country = data['data']['attributes']['entity']['legalAddress']['country']

#         # Create a dictionary with the extracted fields
#         extracted_data = {
#             'id': record_id,
#             'legal_name': legal_name,
#             'jurisdiction': jurisdiction,
#             'legal_address_country': legal_address_country
#         }

#         # Store the extracted data in a JSON file
#         with open('extracted_lei_record.json', 'a') as f:
#             json.dump(extracted_data, f, indent=4)

#         print("Data successfully saved to extracted_lei_record.json")
#     else:
#         print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")


import requests
import json
import pandas as pd

def get_LEI(LID):
    url = 'https://api.gleif.org/api/v1/lei-records/' + str(LID)
    response = requests.get(url)
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

        return extracted_data
    else:
        print(f"Failed to retrieve data for ID {LID}. HTTP Status code: {response.status_code}")
        return None

# Read the IDs from an Excel sheet
input_excel_file = 'test.xlsx'  # Update this with the path to your input Excel file
ids_df = pd.read_excel(input_excel_file)
# Initialize a list to store the extracted data
extracted_data_list = []

# Loop through each ID in the DataFrame and fetch the data
for index, row in ids_df.iterrows():
    LID = row['LEI']  # Assuming the column name in your Excel sheet is 'ID'
    data = get_LEI(LID)
    if data:
        extracted_data_list.append(data)

# Convert the list of dictionaries to a DataFrame
extracted_data_df = pd.DataFrame(extracted_data_list)

# Write the extracted data to a new Excel file
output_excel_file = 'extracted_lei_records.xlsx'  # Update this with the desired output file path
extracted_data_df.to_excel(output_excel_file, index=False)

print(f"Data successfully saved to {output_excel_file}")
