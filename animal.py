from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("Ï can walk and run")
class snake(animal):
    def move(self):
        print("Ï can crawl")
class lion(animal):
    def move(self):
        print("Ï can roar")

edge = human()
edge.move()
s = snake()
s.move()
l = lion()
l.move()