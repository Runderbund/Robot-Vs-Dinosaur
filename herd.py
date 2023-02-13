from dinosaur import Dinosaur as Dino

class Herd:
    def __init__(self):
        self.dinos = [Dino("T-rex"), Dino("Triceratops"), Dino("Archaeopteryx")]
        self.name = "The Herd"
        # Could give health/attack ranges
            # Or a single number each and do +/- 50% in assignment

    def check_dinos_left(self):
        return len(self.dinos) > 0

    def remove_dino(self, index):
        self.dinos.pop(index)