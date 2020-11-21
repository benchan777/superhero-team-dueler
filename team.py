import random
from hero import Hero

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and
            an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
        If Hero isn't found, return 0.
        '''
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        
        if not foundHero:
            return 0

    def view_all_heroes(self):
        ''' Prints out all heroes to the console. '''
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        ''' Add Hero object to self.heroes. '''
        self.heroes.append(hero)

    def stats(self):
        ''' Print team statistics '''
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths += 1
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health '''
        for hero in self.heroes:
            hero.current_health(health)

    def attack(self, other_team):
        ''' Battle each team against each other. '''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            random_hero.fight(random_opponent)

            if random_hero.current_health > random_opponent.current_health:
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)