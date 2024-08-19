class Person:
    def __init__(self, name:str, designation:str) -> object:
        self.name = name
        self.designation = designation
    
    def learn(self) -> None:
        print("I'm learning")
        return
    
    def walk(self) -> None:
        print("I walk with 2 legs")
        return

class Programmer(Person):
    def __init__(self, name:str, designation:str, language:str):
        super().__init__(name, designation)
        self.language = language
    
    def learn(self) -> None:
        print("I'm learning by writing code!")
        return
    
    def programming(self)->None:
        print(f"I'm programming in {self.language}")
        return

class Dancer(Person):
    def __init__(self, name:str, designation:str, genre:str):
        super().__init__(name, designation)
        self.genre = genre
    
    def learn(self) -> None:
        print("I'm learning by dancing!")
        return
    
    def dancing(self)->None:
        print(f"I'm dancing in {self.genre}")
        return

programmer1 = Programmer("Tim", "Programmer", "Python")
dancer1 = Dancer("Jane", "Dancer", "Ballet")

# Testing walk() function. Even though walk() is not defined in subclass, we can still call it as our subclass inherits from the Person class.
programmer1.walk() #Expected Output: I walk with 2 legs
dancer1.walk() # Exprected Output: I walk with 2 legs

#Testing learn() function. We perform method overriding by writing a specific implementation of the learn() method in our subclass.
programmer1.learn() #Expected Output: I'm learning by writing code!
dancer1.learn() #Expected Output: I'm learning by dancing!

#Testing class specific methods (ie programming() and dancing())
programmer1.programming() #Expected Output: I'm programming in Python
dancer1.dancing() #Expected Output: I'm dancing in Ballet

    