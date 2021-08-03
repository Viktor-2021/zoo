class Animal:
    def __init__(self, nombre, edad, habitat, nivel_salud=0, nivel_felicidad=0):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.nivel_salud = nivel_salud
        self.nivel_felicidad = nivel_felicidad
        
   
    def alimentacion(self):
        self.nivel_salud +=10      
        self.nivel_felicidad +=10
                
        return self

    def display_info(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad} \nN_salud:{self.nivel_salud}\nN_felicidad: {self.nivel_felicidad}\nHabitat: {self.habitat},"


#perro=Animal("juan", 25, "Rahue Alto", 10, 10)
#perro.alimentacion()
#print(perro.display_info())



