from personaje import Personaje

class Hombre(Personaje):
    
    def __init__(self, nombre, nivel, altura, edad):
        super().__init__(nombre, nivel, altura)
        self.edad = edad
        
    def __str__(self):
        return super().__str__() + f'; Edad: {self.edad}'
    