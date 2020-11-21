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

    def create_ability(self):
        ''' Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")

        return Ability(name, max_damage)

    def create_weapon(self):
        ''' Prompt user for Weapon information.
            return Weapon with values from user input
        '''
        name = input("What is the weapon name? ")
        max_damage = input("What is the weapon's max damage? ")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What is the armor name? ")
        max_block = input("What is the max block of the piece of armor? ")

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               hero.add_ability(self.create_ability())
           elif add_item == "2":
               hero.add_weapon(self.create_weapon())
           elif add_item == "3":
               hero.add_armors(self.create_armor())
        return hero