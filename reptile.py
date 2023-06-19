# Showcasing inheritance

from animal import Animal

class Reptile(Animal):
    def __int__(self):
        super().__init__() # intialises the parent/nase class - inherit everything from Animal
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles have four legs
        self.heart_chambers = [3,4]
        self.amniotic_eggs = None # Not all reptiles have four legs

    def __seek_heat(self):
        return "it's chilly outside, i need a sunbed"

    def _show_seek_heat(self):
        print(self.__seek_heat())

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("May aswell use it")

    def attract_mate_through_scent(self):
        print("Time to put on the aftershave")




bulbasaur = Reptile()
bulbasaur._show_seek_heat()

# bulbasaur.hunt() # Reptile method
# bulbasaur.breathe() # Animal method



