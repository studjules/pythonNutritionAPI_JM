
class AppUser():
    def __init__(self, name="name", weight=0, Lifestyle=None, allergies=None, dislikes=None):
        self.name = name
        self.weight = weight
        self.Lifestyle = Lifestyle
        self.allergies = allergies
        self.dislikes = dislikes


    def enter_details(self):
        # Enter the user details
        while True:
            try:
                self.name = input("What is your name? ")
                if not self.name.isalpha():
                    raise ValueError("Name must contain only letters.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                self.weight = float(input("What is your weight? "))
                if self.weight < 30:
                    raise ValueError("Weight cannot be below 30.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                self.lifestyle = input("What is your lifestyle? (passive, moderate, active, sporty) ")
                if self.lifestyle not in ["passive", "moderate", "active", "sporty"]:
                    raise ValueError("Lifestyle must be one of: passive, moderate, active, sporty.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")


        while True:
            try:
                self.allergies = input("What are your allergies?(if you have none, type none) ")
                if not self.allergies.isalpha():
                    raise ValueError("Allergies must contain only letters.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                self.dislikes = input("What foods do you dislike? If you dislike none, type none. ")
                if not self.dislikes.isalpha():
                    raise ValueError("Dislikes must contain only letters.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    @property
    def name(self):
        return self._name
    def weight(self):
        return self._weight
    def lifestyle(self):
        return self._lifestyle
    def allergies(self):
        return self._allergies
    def dislikes(self):
        return self._dislikes

    @name.setter
    def name(self, new_name):
        self._name = new_name
    def weight(self, new_weight):
        self._weight = new_weight
    def lifestyle(self, new_lifestyle):
        self._lifestyle = new_lifestyle
    def allergies(self, new_allergies):
        self._allergies = new_allergies
    def dislikes(self, new_dislikes):
        self._dislikes = new_dislikes



if __name__ == "__main__":
    user = AppUser()
    user.enter_details()
    print(user.name)
    print(user.weight)
    print(user.lifestyle)
    print(user.allergies)
    print(user.dislikes)




