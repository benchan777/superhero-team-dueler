from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        ''' This method returns a random value between
            one half to the full attack power of the weapon
        '''
        half_effectiveness = self.max_damage // 2
        random_value = random.randint(half_effectiveness, self.max_damage)
        return random_value