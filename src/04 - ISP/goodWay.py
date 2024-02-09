from abc import ABC, abstractmethod

"""
Interface Segregation Principle(ISP)

Rather than writing generic interface, for each responsiblity there should be seperate interface
"""

class Walker(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass


class Human(Walker, Swimmer):    
    def swim(self):
        print('Human can swim')

    def walk(self):
        print('Human can walk')


class Whale(Swimmer):
    def swim(self):
        print('Whale can swim')


if __name__ == '__main__':
    human = Human()
    human.swim()
    human.walk()

    whale = Whale()
    whale.swim()