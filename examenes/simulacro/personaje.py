class Personaje:
    
    def __init__(self, nombre, nivel, altura):
        self.nombre = nombre
        self.nivel = nivel
        self.altura = altura
        
    def subir_nivel(self):
        self.nivel += 1
        print(f'Nivel incrementado en 1, Nivel actual: {self.nivel}')
        
    def __str__(self):
        return f'Nombre: {self.nombre}; Nivel: {self.nivel}; Altura: {self.altura}'
        
        