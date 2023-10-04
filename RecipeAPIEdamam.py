import requests
from bs4 import BeautifulSoup

class RecipeAPI:
    def __init__(self, app_id, app_key, base_url):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = base_url

    def search_recipes(self, meal_type):
        # Set the endpoint and query parameters
        endpoint = self.base_url
        health_labels = []
        diet = ["high-protein"]
        dish_type = ["Main course"]
        params = {
            "type": "public",
            "health": health_labels,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "diet": diet,
            "mealType": [meal_type],
            "dishType": dish_type,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse and work with the response JSON data
            data = response.json()
            # Access the first 100 recipes in the response
            recipes = [hit["recipe"] for hit in data.get("hits", [])[:100]]

            # Extract and return information about the recipes
            result = []
            for recipe in recipes:
                recipe_info = {
                    "Title": self.get_recipe_title(recipe.get("url", {})),
                    "Calories(kcal)": recipe.get("totalNutrients", {}).get('ENERC_KCAL', {}).get('quantity'),
                    "Zinc(mg)": recipe.get("totalNutrients", {}).get('ZN', {}).get('quantity'),
                    "FAT(g)": recipe.get("totalNutrients", {}).get('FAT', {}).get('quantity'),
                    "SUGAR(g)": recipe.get("totalNutrients", {}).get('SUGAR', {}).get('quantity'),
                    "Protein(g)": recipe.get("totalNutrients", {}).get('PROCNT', {}).get('quantity'),
                    "Magnesium(mg)": recipe.get("totalNutrients", {}).get('MG', {}).get('quantity'),
                    "Iron(mg)": recipe.get("totalNutrients", {}).get('FE', {}).get('quantity'),
                    "Fiber(g)": recipe.get("totalNutrients", {}).get('FIBTG', {}).get('quantity'),
                    "Carbohydrates(g)": recipe.get("totalNutrients", {}).get('CHOCDF', {}).get('quantity'),
                    "URL": recipe.get("url", {}),
                }
                result.append(recipe_info)

            return result
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}



if __name__ == "__main__":
    # Example usage:
    app_id = "26290cfb"
    app_key = "57174ba13d0a17c660851f47e9d59280"
    base_url = "https://api.edamam.com/api/recipes/v2"
    recipe_searcher = RecipeAPI(app_id, app_key, base_url)

    breakfast_recipes = recipe_searcher.search_recipes("breakfast")
    lunch_recipes = recipe_searcher.search_recipes("lunch")
    dinner_recipes = recipe_searcher.search_recipes("dinner")

    print("Number of breakfast recipes:", len(breakfast_recipes))
    print("breakfast recipes:")
    print(breakfast_recipes)
    print("Number of lunch recipes:", len(lunch_recipes))
    print("lunch recipes:")
    print(lunch_recipes)
    print("Number of dinner recipes:", len(dinner_recipes))
    print("dinner recipes:")
    print(dinner_recipes)


