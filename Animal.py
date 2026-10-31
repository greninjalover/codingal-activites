from abc import ABC,  abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither and crawl")

snake_obj=Snake()
snake_obj.move()
human_obj=Human()
human_obj.move()
