import requests

class Recipelists:
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

        # Return the list of recipe information
            br_result = []
            for i in range(len(br_recipes)):
                recipe_info = {
                    "Calories(kcal)": br_recipes[i].get("totalNutrients", {}).get('ENERC_KCAL', {}).get('quantity'),
                    "Zink(mg)": br_recipes[i].get("totalNutrients", {}).get('ZN', {}).get('quantity'),
                    "FAT(g)": br_recipes[i].get("totalNutrients", {}).get('FAT', {}).get('quantity'),
                    "SUGAR(g)": br_recipes[i].get("totalNutrients", {}).get('SUGAR', {}).get('quantity'),
                    "Protein(g)": br_recipes[i].get("totalNutrients", {}).get('PROCNT', {}).get('quantity'),
                    "Magnesium(mg)": br_recipes[i].get("totalNutrients", {}).get('MG', {}).get('quantity'),
                    "Iron(mg)": br_recipes[i].get("totalNutrients", {}).get('FE', {}).get('quantity'),
                    "Fiber(g)": br_recipes[i].get("totalNutrients", {}).get('FIBTG', {}).get('quantity'),
        	        "Carbohydrates(g)": br_recipes[i].get("totalNutrients", {}).get('CHOCDF', {}).get('quantity'),
                }
                br_result.append(recipe_info)

            return br_result
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}

    import requests
    def search_lunch_recipe(self):
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

            # Extract and return information about the first 100 recipes
            lu_result = []
            for i in range(len(lu_recipes)):
                recipe_info = {
                    "Calories": lu_recipes[i].get("totalNutrients", {}).get('ENERC_KCAL', {}).get('quantity'),
                    "Recipe Image": lu_recipes[i].get("image"),
                    "Recipe Ingredients": lu_recipes[i].get("ingredientLines"),
                    "URL": lu_recipes[i].get("url"),
                }
                lu_result.append(recipe_info)

            # Return the list of recipe information
            return lu_result

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

            #Extract list of recipes
            di_result = []
            for i in range(len(di_recipes)):
                recipe_info = {
                    "Calories": di_recipes[i].get("totalNutrients", {}).get('ENERC_KCAL', {}).get('quantity'),
                    
                }
                di_result.append(recipe_info)

            return di_result
        else:
            # Handle API request error (e.g., return an error message)
            return {"Error": response.status_code, "Message": response.text}


if __name__ == "__main__":
    # Example usage:
    app_id = "26290cfb"
    app_key = "57174ba13d0a17c660851f47e9d59280"
    recipe_searcher = Recipelists(app_id, app_key)

    recipe_breakfast = recipe_searcher.search_breakfast_recipe()
    recipe_lunch = recipe_searcher.search_lunch_recipe()
    recipe_dinner = recipe_searcher.search_dinner_recipe()

   
    print("breakfast recipes:")
    print(recipe_breakfast)


