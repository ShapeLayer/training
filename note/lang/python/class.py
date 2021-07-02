from abc import *   # Abstract Class

class entity(metaclass=ABCMeta): # Set Meta Class
    def __init__(self, life):
        self.life = life

    @abstractmethod
    def get_life(self):
        pass

class non_hostile:
    def __init__(self, tame_condition):
        self.tame_condition = tame_condition

    def tame(self):
        print(self.tame_condition)
        pass

class animal(entity, non_hostile): # Python class can inherit multiple.
    def __init__(self, life, tame_condition):
        entity.__init__(self, life)
        non_hostile.__init__(self, tame_condition) # Init parent class and inherit.

    def tame(self): # Method overriding
        super().tame() # Run parent method
        print(self.tame_condition, 'wang') # Run method
    
    def get_life(self): # Abstract Method should be overrided.
        print(self.life)

if __name__ == '__main__':
    rabbit = animal(life=15, tame_condition='당근 [3, 10]개')
    rabbit.tame()
    print(animal.mro()) # Print inherit list
