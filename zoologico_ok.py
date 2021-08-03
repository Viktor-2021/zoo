from animales import Animal
from tigre import Tigre
from tiburon import Tiburon
from lagarto import Lagarto
import os

class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        print(self.name)
                    
    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.nombre == new_animal.nombre:
                return False
        self.animals.append(new_animal)
        return True

    def liberar_animal(self, name):
        for animal in self.animals:
            if animal.nombre == name.nombre:
                print(animal.display_info() + ' y acaban de liberarme en una reserva salvaje')
                self.animals.remove(animal)
            else:
                False
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal.display_info())
            print('*'*100)

