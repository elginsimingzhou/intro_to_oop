class Dog:
    def __init__(self, name:str, age:int):
        """Dog constructor that creates Dog Objects.

        Args:
        name: A dog's name. (Private)
        age: A dog's age. (Private)

        Returns:
        Dog object reference

        """
        self.__name = name
        self.__age = age
    
    def get_name(self)->str:
        return self.__name

    def get_age(self)->int:
        return self.__age
    
    def set_name(self, new_name:str)->None:
        self.__name = new_name
        return
    
    def set_age(self, new_age:int) -> None:
        self.__age = new_age
        return
    
    def bark(self) -> None:
        print(f"Woof Woof! My name is {self.__name} and I am {self.__age} years old")
        return

#Create a new Dog Object
dog1 = Dog("Tim", 1)
#TODO: Try getting private attribute "name" without using the getter method.
#print(dog1.__name) #Expected output: AttributeError: 'Dog' object has no attribute '__name'
print(dog1.get_name) #Expected output: Tim

#TODO: Try setting private attribute "age" without using the setter method.
dog1.__age = 2 
print(dog1.get_age()) #Expected output: 1
dog1.set_age(2)
print(dog1.get_age()) #Expected output: 2