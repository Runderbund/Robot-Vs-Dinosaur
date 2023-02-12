from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_1 = Dinosaur("T-rex")
        self.dino_2 = Dinosaur("Triceratops")
        self.dino_3 = Dinosaur("Archaeopteryx")
        # Could give health/attack ranges
            # Or a single number each and do +/- 50% in assignment