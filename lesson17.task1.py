class Animall:
    def talk(self):
        pass

class Dog(Animall):
    def talk(self):
        return "Гав-гав"

class Cat(Animall):
    def talk(self):
        return "Мяу"

def make_animal_talk(animal):
    print(animal.talk())

dog = Dog()
cat = Cat()

make_animal_talk(dog)
make_animal_talk(cat)
