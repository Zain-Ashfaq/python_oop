# Animal class

class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath at a time, in and out")

    def eat(self):
        print("Nom nom nom")

    def procreate(self):
        print("find someone")

    def move(self):
        print("i moved")

# breathe is abstracted
cat = Animal()
#cat.breathe()