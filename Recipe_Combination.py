from RecipeAPIEdamam import RecipeAPI
from itertools import product
import random
class Recipe_optimizer(RecipeAPI):
    def __init__(self, app_id, app_key, base_url):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = base_url

    def combine_optimize(self):
        breakfast_recipes = self.search_recipes("breakfast")[:10]
        lunch_recipes = self.search_recipes("lunch")[:10]
        dinner_recipes = self.search_recipes("dinner")[:10]

        all_combinations = product(breakfast_recipes, lunch_recipes, dinner_recipes)
        # Initialize a list to store the results
        results = []

        # Iterate through the combinations and sum up the values for each combination
        for combo in all_combinations:
            combined_values = {}
            for recipe in combo:
                for key, value in recipe.items():
                    if key in combined_values:
                        combined_values[key] += value
                    else:
                        combined_values[key] = value
            results.append(combined_values)
        valid_recipe_combinations = []
        for i, result in enumerate(results):
            if result["Protein(g)"] >= 80 and result["FAT(g)"] <= 80 and result["Calories(kcal)"] >= 2000:
                valid_recipe_combinations.append(result)
            else:
                continue
        print(f"The valid recipes are{valid_recipe_combinations[:]}")
        return valid_recipe_combinations


if __name__ == '__main__':

    app_id = "26290cfb"
    app_key = "57174ba13d0a17c660851f47e9d59280"
    base_url = "https://api.edamam.com/api/recipes/v2"

    object = Recipe_optimizer(app_id, app_key, base_url)
    object.combine_optimize()


