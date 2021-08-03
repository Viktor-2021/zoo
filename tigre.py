from animales import Animal


class Tigre(Animal):
    def __init__(self, nombre, edad, habitat, nadar, nivel_salud=0, nivel_felicidad=0):
        super().__init__(nombre, edad, habitat, nivel_salud, nivel_felicidad)
        self.nadar=nadar

    def alimentacion(self, alimento):
                 
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

    def display_info(self):
        return super().display_info() + (' se nadar' if self.nadar==True else ' aún no se nadar')