# Showcasing Encapsulation
from reptile import Reptile
class Snake(Reptile):
    def __int__(self):
        super().__int__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None # Not all snakes have venom
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("Do i say it smells or taste nice?")


sidney = Snake()


sidney.breathe() # Animal
sidney._seek_heat() # Reptile
sidney.use_tongue_to_smell() # Snake

# Encapsulation is also really good for protecting important variables/objects

# Types of modifiers in Python -

# Public - Anyone anywhere can use it
# Private - Accessible only within the class itself
# Protected - Accessible within the class and it's subclasses


