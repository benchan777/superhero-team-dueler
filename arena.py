from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        ''' Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")