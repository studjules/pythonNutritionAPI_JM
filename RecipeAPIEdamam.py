import requests

class Recipe:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = 'https://api.edamam.com/api/recipes/v2'

    def search_breakfast_recipe(self):
        # Set the endpoint and query parameters
        endpoint = self.base_url
        health_labels = []
        diet = ["high-protein"]
        meal_type = ["breakfast"]
        dish_Type = ["Main course"]
        params = {
            "type": "public",
            "health": health_labels,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "diet": diet,
            "mealType": meal_type,
            "dishType": dish_Type,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and work with the response JSON data
            data = response.json()
            # Access the first recipe in the response
            br_recipes = [hit["recipe"] for hit in data.get("hits", [])[:100]]

            # Extract and return information about the first recipe
            return {

                "totalNutrients": br_recipes[0].get("totalNutrients"),
                "Recipe Name": br_recipes[0].get("label"),
                "Recipe Image": br_recipes[0].get("image"),
                "Recipe Ingredients": br_recipes[0].get("ingredientLines"),
                "URL": br_recipes[0].get("url"),
                "Listlength": len(br_recipes),
            }
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}

    def search_lunch_recipe(self):
        # Set the endpoint and query parameters
        endpoint = self.base_url
        health_labels = []
        diet = ["high-protein"]
        meal_type = ["lunch"]
        dish_Type = ["Main course"]
        params = {
            "type": "public",
            "health": health_labels,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "diet": diet,
            "mealType": meal_type,
            "dishType": dish_Type,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and work with the response JSON data
            data = response.json()
            # Access the first recipe in the response
            lu_recipes = [hit["recipe"] for hit in data.get("hits", [])[:100]]

            # Extract and return information about the first recipe
        for i in  len(lu_recipes):
            return {
                "Calories": lu_recipes[i].get("totalNutrients",{}).get('ENERC_KCAL',{}).get('quantity'),
                "Recipe Image": lu_recipes[i].get("image"),
                "Recipe Ingredients": lu_recipes[i].get("ingredientLines"),
                "URL": lu_recipes[i].get("url"),
                "Listlength": len(lu_recipes),
            }
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}

    def search_dinner_recipe(self):
        # Set the endpoint and query parameters
        endpoint = self.base_url
        health_labels = []
        diet = ["high-protein"]
        meal_type = ["dinner"]
        dish_Type = ["Main course"]
        params = {
            "type": "public",
            "health": health_labels,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "diet": diet,
            "mealType": meal_type,
            "dishType": dish_Type,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and work with the response JSON data
            data = response.json()
            # Access the first recipe in the response
            di_recipes = [hit["recipe"] for hit in data.get("hits", [])[:100]]

            # Extract and return information about the first recipe
            return {

                "Recipe Name": di_recipes[1].get("label"),
                "Recipe Image": di_recipes[1].get("image"),
                "Recipe Ingredients": di_recipes[1].get("ingredientLines"),
                "URL": di_recipes[1].get("url"),
                "Listlength": len(di_recipes),

            }
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}


if __name__ == "__main__":
    # Example usage:
    app_id = "81f8d87f"
    app_key = "25e930457335a2fdcf2d293c6de3fcde"
    recipe_searcher = Recipe(app_id, app_key)

    recipe_breakfast = recipe_searcher.search_breakfast_recipe()
    recipe_lunch = recipe_searcher.search_lunch_recipe()
    recipe_dinner = recipe_searcher.search_dinner_recipe()

    print(recipe_breakfast)
    print(recipe_lunch)
    print(recipe_dinner)


