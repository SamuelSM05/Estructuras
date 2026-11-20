class PersonajeTeletubby:
    saludo_oficial = "Tubby abrazo"
    
    def __init__(self,nombre, color, antena, objeto_favorito):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        
        self.__hambre = 50
        self.__nivel_felicidad = 100
        
         
    def saludar(self):
        print(f"Me llamo {self.nombre} soy de color {self.color} y mi antena tiene forma de {self.antena} ")
        print(self.saludo_oficial)
    
    def jugar(self):
        print(f"{self.nombre} esta jugando con su {self.objeto_favorito}")
        self.__hambre +=20
        self.__nivel_felicidad +=10
        
    def comer_tubby_papilla(self):
        print(f"{self.nombre} se esta alimentando")
        self.__hambre = 0
        
    def ver_estado(self):
        print(f"{self.nombre}:\n Felicidad: {self.__nivel_felicidad}\n Hambre: {self.__hambre}")
    
    def __str__(self):
        return f"--------------------------\n Nombre: {self.nombre}\n Color: {self.color}\n Forma de antena: {self.antena}\n Objeto favorito: {self.objeto_favorito}\n --------------------------"
        