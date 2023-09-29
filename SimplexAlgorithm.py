
from docplex.mp.model import Model

class optimizer:
    def __init__(self):
        self.model = Model(name="Nutrientoptimizer")
        # Define the decision variables with different names
        self.Calories_var = self.model.continuous_var(name="Calories")
        self.Fat_var = self.model.continuous_var(name="Fat")
        self.Protein_var = self.model.continuous_var(name="Protein")


    def add_constraints(self, recipe_info):
        # Add constraints
        self.model.add_constraint(self.Calories_var >= recipe_info["Calories"])
        self.model.add_constraint(self.Fat_var >= recipe_info["Fat"])
        self.model.add_constraint(self.Protein_var >= recipe_info["Protein"])
        self.model.add_constraint(self.Calories_var <= 2000)
        self.model.add_constraint(self.Fat_var <= 65)

    def add_objective(self):
        # Add objective
        self.model.maximize(self.Protein_var)

    def solve(self):
        # Solve the model
        self.model.solve()
        return self.model.solution

if __name__ == "__main__":
    # Create an instance of the optimizer class
    opt = optimizer()
    # Define the recipe information
    recipe_info = {"Calories": 100, "Fat": 10, "Protein": 20}
    # Add constraints
    opt.add_constraints(recipe_info)
    # Add objective
    opt.add_objective()
    # Solve the model
    solution = opt.solve()
    # Print the solution
    print(solution)
    # Print the objective value
    print(solution.objective_value)
    # Print the decision variables
    print(solution.get_value(opt.Calories_var))
    print(solution.get_value(opt.Fat_var))
    print(solution.get_value(opt.Protein_var))