import requests

# Edamam API credentials
app_id = '1c5704dc'
app_key = 'd700286edc0465fb52ba9a9fc07cd010'

# Base URL for Edamam Food Database API
base_url = 'https://api.edamam.com/api/recipes/v2'

# Define your query parameters
query_params = {
    'ingr': 'pear',  # Example query, you can change this
    'app_id': app_id,
    'app_key': app_key
}

try:
    # Make a GET request to the Edamam API
    response = requests.get(base_url, params=query_params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)
    else:
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
