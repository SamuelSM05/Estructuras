from personaje import Personaje

class Elfo(Personaje):
    TIPOS_VALIDOS = {"SILVANO", "BOSQUE", "LUZ", "OSCURO"}
    
    def __init__(self, nombre, nivel, altura, tipo_elfo):
        if tipo_elfo not in self.TIPOS_VALIDOS:
            raise ValueError(f"tipo_elfo debe ser uno de: {', '.join(self.TIPOS_VALIDOS)}")
        super().__init__(nombre, nivel, altura)
        self.tipo_elfo = tipo_elfo
        
        
    def __str__(self):
        return super().__str__() + f'; TipoElfo: {self.tipo_elfo}'
        