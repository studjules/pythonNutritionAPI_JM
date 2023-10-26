import tkinter as tk
from Recipe_Combination import Recipe_optimizer

class RecipeAppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Optimizer")

        # Create input fields
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.lifestyle_label = tk.Label(root, text="Lifestyle:")
        self.lifestyle_label.pack()
        self.lifestyle_entry = tk.Entry(root)
        self.lifestyle_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Create the "Optimize" button
        self.optimize_button = tk.Button(root, text="Optimize", command=self.optimize)
        self.optimize_button.pack()

    def optimize(self):
        app_id = "26290cfb"
        app_key = "57174ba13d0a17c660851f47e9d59280"
        base_url = "https://api.edamam.com/api/recipes/v2"

        name = self.name_entry.get()
        weight = float(self.weight_entry.get())
        lifestyle = self.lifestyle_entry.get()

        user = Recipe_optimizer(app_id, app_key, base_url, name, weight, lifestyle)
        result = user.combine_optimize()
        self.result_label.config(text=f"Optimized recipe for {name}:\n{result}")

if __name__ == '__main__':
    root = tk.Tk()
    app = RecipeAppUI(root)
    root.mainloop()

