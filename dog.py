class Dog:
    def __init__(self, name:str, age:int):
        """Dog constructor that creates Dog Objects.

        Args:
        name: A dog's name. 
        age: A dog's age.

        Returns:
        Dog object reference

        """
        self.name = name
        self.age = age
    
    def get_name(self)->str:
        return self.name

    def get_age(self)->int:
        return self.age
    
    def set_name(self, new_name:str)->None:
        self.name = new_name
        return
    
    def set_age(self, new_age:int) -> None:
        self.age = new_age
        return
    
    def bark(self) -> None:
        print(f"Woof Woof! My name is {self.name} and I am {self.age} years old")
        return

#Create a new Dog Object
dog1 = Dog("Tim", 1)
print(dog1) #Expected output: Similar to <__main__.Dog object at 0x000001C90886E8D0> 
print(dog1.get_name()) #Expected output: Tim
print(dog1.get_age()) #Expected output: 1
dog1.set_name('Timmy') 
dog1.set_age(2)
dog1.bark() #Expected output: Woof Woof! My name is Timmy and I am 2 years old 