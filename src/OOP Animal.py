# OOP Approach

class Animal:
    def __init__(self, species, diet, lifespan, is_oviparous):
        self.species = species
        self.diet = diet
        self.lifespan = lifespan
        self.is_oviparous = is_oviparous  # Does it lay eggs?

    def make_sound(self):
        return "What does this animal say?"

    def display_info(self):
        return (f"Species: {self.species}, Diet: {self.diet}, Lifespan: {self.lifespan} years, "
                f"Lays Eggs: {
                'Yes' if self.is_oviparous else 'No'
                }")


# Mammal is an animal
class Mammal(Animal):
    def __init__(self, species, diet, lifespan, fur_color, warm_blooded=True):
        # Mammals do not lay eggs.
        super().__init__(species, diet, lifespan, is_oviparous=False)
        self.fur_color = fur_color
        self.warm_blooded = warm_blooded

    def regulate_temperature(self):
        return (f"{self.species} is {'warm-blooded' if self.warm_blooded else 'cold-blooded'} and regulates its "
                f"temperature accordingly.")


# Lion is a Mammal
class Lion(Mammal):
    def __init__(self, fur_color="Golden"):
        super().__init__(species="Lion", diet="Carnivore", lifespan=14, fur_color=fur_color)

    def make_sound(self):
        return "Roar! 🦁"

    def hunt(self):
        return "The lion is hunting in the savanna."


# Test out Lion()
# Lion lion = new Lion();
simba = Lion()

print(simba.display_info())
print(simba.make_sound())
print(simba.regulate_temperature())
print(simba.hunt())
