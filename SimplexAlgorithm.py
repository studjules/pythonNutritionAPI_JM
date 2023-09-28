
from docplex.mp.model import Model

class optimizer:
    def __init__(self):
        self.model = Model(name="Nutrientoptimizer")

    # Define the decision variables
    Calories = self.model.continuous_var(name="Calories")
    Fat = self.model.continuous_var(name="Fat")
    Protein = self.model.continuous_var(name="Protein")

    # Add constraints
    self.model.add_constraint(Calories >= 2000 and Calories <= 2500)
    self.model.add_constraint(Fat >= 60 and Fat <= 65)

    # Add the objective function to the model
    self.model.maximize(Protein)

    # Solve the model
    solution = self.model.solve()