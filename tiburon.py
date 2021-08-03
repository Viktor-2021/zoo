from animales import Animal
class Tiburon(Animal):
    def __init__(self, nombre, edad, habitat, nivel_salud=0, nivel_felicidad=0):
        super().__init__(nombre, edad, habitat, nivel_salud, nivel_felicidad)

    def alimentacion(self, alimento):
        super().alimentacion()           
        if alimento <11:
            self.nivel_felicidad+=round (alimento/2)
            self.nivel_salud+=alimento
            
            return f"Nivel salud: {self.nivel_salud} | Nivel de Felicidad:{self.nivel_felicidad} | No soy feliz"

        elif alimento <=20:
            self.nivel_felicidad +=round(alimento/2)
            self.nivel_salud +=alimento
            return f"Nivel salud: {self.nivel_salud} | Nivel de Felicidad:{self.nivel_felicidad} | Estoy Feliz"
        
        elif alimento <=30:
            self.nivel_felicidad +=round(alimento/2)
            self.nivel_salud +=alimento
            return f"Nivel salud: {self.nivel_salud} | Nivel de Felicidad:{self.nivel_felicidad} | Estoy muy Feliz"
        
        elif alimento >31:
            self.nivel_felicidad +=round(alimento/2)
            self.nivel_salud +=alimento
            return f"Nivel salud: {self.nivel_salud} | Nivel de Felicidad:{self.nivel_felicidad} | No soy feliz, comi mucho!"
       
        
        
