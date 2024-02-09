from abc import ABC, abstractmethod

class Mammals(ABC):
    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Human(Mammals):
    def swim(self):
        print('Human can swim')

    def walk(self):
        print('Human can walk')


class Whale(Mammals):
    def swim(self):
        print('Whale can swim')

    def walk(self):
        print('Whale can\'t walk')


if __name__ == '__main__':
    human = Human()
    human.swim()
    human.walk()

    whale = Whale()
    whale.swim()
    whale.walk()