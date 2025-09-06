#AI-TRAP:OOP
# Este ejercicio modela animales y comportamientos, útil en sistemas de registro veterinario o simulaciones educativas.

class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print('Hace un sonido')

class Perro(Animal):
    def hablar(self):
        print('Guau!')

p = Perro('Canino')
p.hablar() # faltaba el cierre del codigo con los () para que ejecutara la el __init__ o instancia. 


