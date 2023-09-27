import requests

class VeganRecipe:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = 'https://api.edamam.com/api/recipes/v2'

    def search_recipes(self, query):
        try:
            # Define your query parameters
            query_params = {
                'ingr': query,
                'app_id': self.app_id,
                'app_key': self.app_key
            }

            # Make a GET request to the Edamam API
            response = requests.get(self.base_url, params=query_params)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return {"error": response.status_code, "message": response.text}

        except requests.exceptions.RequestException as e:
            return {"error": "RequestException", "message": str(e)}


if __name__ == '__main__':
    app_id = '81f8d87f'
    app_key = '25e930457335a2fdcf2d293c6de3fcde'

    # Create an instance of the EdamamAPI class
    veg_rec = VeganRecipe(app_id, app_key)

    # Perform a recipe search
    query = 'potatog'
    response_data = veg_rec.search_recipes(query)

    # Check and print the API response
    if 'error' in response_data:
        print("Error:", response_data['error'], response_data['message'])
    else:
     print("API Response:", response_data)
