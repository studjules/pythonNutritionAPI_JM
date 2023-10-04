import pulp
from pulp import *

# Create a LP Minimization problem
def calculation():
    
    model = LpProblem("Maximize_Protein", LpMaximize)

    # Create problem Variables
    protein = LpVariable("Protein", lowBound=0, cat='Continuous')
    calories = LpVariable("Calories", lowBound=0, cat='Continuous')
    fat = LpVariable("Fat", lowBound=0, cat='Continuous')
    carbs = LpVariable("Carbs", lowBound=0, cat='Continuous')
    fiber = LpVariable("Fiber", lowBound=0, cat='Continuous')
    sugar = LpVariable("Sugar", lowBound=0, cat='Continuous')
    cholesterol = LpVariable("Cholesterol", lowBound=0, cat='Continuous')
    sodium = LpVariable("Sodium", lowBound=0, cat='Continuous')
    calcium = LpVariable("Calcium", lowBound=0, cat='Continuous')
    potassium = LpVariable("Potassium", lowBound=0, cat='Continuous')
    iron = LpVariable("Iron", lowBound=0, cat='Continuous')
    zinc = LpVariable("Zinc", lowBound=0, cat='Continuous')
    vitamin_a = LpVariable("Vitamin_A", lowBound=0, cat='Continuous')
    vitamin_c = LpVariable("Vitamin_C", lowBound=0, cat='Continuous')
    vitamin_d = LpVariable("Vitamin_D", lowBound=0, cat='Continuous')
    vitamin_b6 = LpVariable("Vitamin_B6", lowBound=0, cat='Continuous')
    vitamin_b12 = LpVariable("Vitamin_B12", lowBound=0, cat='Continuous')

    # Objective Function
    model += protein, "Maximize_Protein"

    # Constraints
    model += calories >= 2000, "Calories"
    model += fat >= 65, "Fat"
    model += carbs >= 300, "Carbs"
    model += fiber >= 25, "Fiber"
    model += sugar >= 50, "Sugar"
    model += cholesterol >= 300, "Cholesterol"  
    model += sodium >= 2400, "Sodium"
    model += calcium >= 1000, "Calcium"
    model += potassium >= 3500, "Potassium"
    model += iron >= 8, "Iron"
    model += zinc >= 15, "Zinc"
    model += vitamin_a >= 900, "Vitamin_A"
    model += vitamin_c >= 90, "Vitamin_C"
    model += vitamin_d >= 20, "Vitamin_D"
    model += vitamin_b6 >= 2, "Vitamin_B6"
    model += vitamin_b12 >= 6, "Vitamin_B12"

    # Solve the problem
    status = model.solve()