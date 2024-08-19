from typing import List

class Animal:
    def speak(self) -> None:
        print("I am speaking")
        return

class Dog(Animal):
    def speak(self) -> None:
        print("Woof Woof")
        return

class Cat(Animal):
    def speak(self) -> None:
        print("Meow Meow")
        return

class Duck(Animal):
    def speak(self) -> None:
        print("Quack Quack")
        return

def main():
    animals : List[Animal] = []
    dog = Dog()
    cat = Cat()
    duck = Duck()
    animals.append(dog)
    animals.append(cat)
    animals.append(duck)

    for animal in animals:
        animal.speak()

main() 
# Test speak() method: Notice that each object is doing the same thing (ie speak() ) in a different implementation. This is polymorphism.
#Expected Ouput: 
# Woof Woof
# Meow Meow
# Quack Quack
