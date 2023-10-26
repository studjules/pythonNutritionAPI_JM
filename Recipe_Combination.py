from AppUser import AppUser
from RecipeAPIEdamam import RecipeAPI
from itertools import product
import random
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
class Recipe_optimizer(RecipeAPI):
    def __init__(self, app_id, app_key, base_url, app_user):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = base_url
        self.app_user = app_user
        self.name, self.weight, self.lifestyle, self.allergies, self.dislikes = self.app_user.get_profile()

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
                        if key == "Url":
                            combined_values["Url"] += f" {value}"
                        if key == "Meal_type":
                            combined_values["Meal_type"] += f" {value}"
                        else:
                            combined_values[key] += value
                    else:
                        combined_values[key] = value
            results.append(combined_values)
        valid_recipe_combinations = []

        if self.lifestyle == "active":
            activity = 1.2
        if self.lifestyle == "moderate":
            activity = 1
        if self.lifestyle == "passive":
            activity = 0.8
        if self.lifestyle == "sporty":
            activity = 1.4

        for i, result in enumerate(results):
            if result["Protein(g)"] >= 0.8 * self.weight and result["FAT(g)"] <= 60 and result["Calories(kcal)"] >= 20 * self.weight * activity and result["SUGAR(g)"] <= 10 \
                    and result["Iron(mg)"] >= 13:
                valid_recipe_combinations.append(result)
            else:
                continue
        random_int = random.randint(0, len(valid_recipe_combinations)-1)
        print(f"Here is {self.name}'s valid Recipe-combination of the day{valid_recipe_combinations[random_int]}")
        # Extract specific keys and values
        gramm_plot_keys = [key for key in valid_recipe_combinations[random_int].keys() if "(g)" in key]
        x_values_g = [key for key in gramm_plot_keys]
        y_values_g = [valid_recipe_combinations[random_int][key] for key in gramm_plot_keys]

        mg_plot_keys = [key for key in valid_recipe_combinations[random_int].keys() if "(mg)" in key]
        x_values_mg = [key for key in mg_plot_keys]
        y_values_mg = [valid_recipe_combinations[random_int][key] for key in mg_plot_keys]




        # Your code here to define x_values and y_values

        # Create a subplot with two charts
        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=[f"{self.name}'s nutrients of the day in g", f"{self.name}'s nutrients of the day in mg"])

        # Add the bar charts
        fig.add_trace(go.Bar(x=x_values_g, y=y_values_g), row=1, col=1)
        fig.add_trace(go.Bar(x=x_values_mg, y=y_values_mg), row=1, col=2)
        #update y label for the second chart
        fig.update_yaxes(title_text="mg", row=1, col=2)
        #update x label for the second chart
        fig.update_xaxes(title_text="nutrients", row=1, col=2)
        #update y label for the first chart
        fig.update_yaxes(title_text="g", row=1, col=1)
        #update x label for the first chart
        fig.update_xaxes(title_text="nutrients", row=1, col=1)

        # Update the layout
        fig.update_layout(showlegend=False)  # You can customize other layout options here

        # Show the subplot
        fig.show()


        return valid_recipe_combinations




if __name__ == '__main__':

    app_id = "26290cfb"
    app_key = "57174ba13d0a17c660851f47e9d59280"
    base_url = "https://api.edamam.com/api/recipes/v2"

    user = AppUser()
    user.enter_details()
    object = Recipe_optimizer(app_id, app_key, base_url, user)
    object.combine_optimize()


