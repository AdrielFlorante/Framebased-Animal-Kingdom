# OOP Approach with Frame-Based Concept and Type Hints
class Animal:
    def __init__(self, species: str, diet: str, lifespan: int, is_oviparous: bool):
        self.species: str = species
        self.diet: str = diet
        self.lifespan: int = lifespan
        self.is_oviparous: bool = is_oviparous  # Does it lay eggs?

    def make_sound(self) -> str:
        return "What does this animal say?"

    def display_info(self) -> str:
        return (f"Species: {self.species}, Diet: {self.diet}, Lifespan: {self.lifespan} years, "
                f"Lays Eggs: {'Yes' if self.is_oviparous else 'No'}")


# Mammal is an Animal
class Mammal(Animal):
    def __init__(self, species: str, diet: str, lifespan: int, fur_color: str, warm_blooded: bool = True):
        super().__init__(species, diet, lifespan, is_oviparous=False)
        self.fur_color: str = fur_color
        self.warm_blooded: bool = warm_blooded

    def regulate_temperature(self) -> str:
        return (f"{self.species} is {'warm-blooded' if self.warm_blooded else 'cold-blooded'} and regulates its "
                f"temperature accordingly.")


# Lion is a Mammal
class Lion(Mammal):
    def __init__(self, fur_color: str = "Golden"):
        super().__init__(species="Lion", diet="Carnivore", lifespan=14, fur_color=fur_color)

    def make_sound(self) -> str:
        return "Roar! 🦁"

    def hunt(self) -> str:
        try:
            from src.Hunting.Hunting import Hunting

            hunting = Hunting().hunt(self)
            return "The lion is hunting in the savanna."
        except TypeError as e:
            print("Hunting animation was closed.")  # Just prints the message
            return "The lion has stopped hunting."

# WhiteLion is a Lion (4th Layer)
class WhiteLion(Lion):
    def __init__(self, fur_color: str = "White"):
        super().__init__(fur_color=fur_color)

    def camouflage(self) -> str:
        return "The white lion blends in with the savanna during winter."


# Test out WhiteLion()
kiara = WhiteLion()

print(kiara.display_info())  # Inherits from Lion, Mammal, and Animal
print(kiara.make_sound())    # Still "Roar! 🦁"
print(kiara.regulate_temperature())  # Still from Mammal

# Hunting.hunt() causes an error with tkinter when the window is closed, this is only a bandaid solution
try:
    print(kiara.hunt())  # Still inherited from Lion, will show an animation
except HuntingError as e:
    print(f"Error: {e}")

print(kiara.camouflage())    # Unique to WhiteLion