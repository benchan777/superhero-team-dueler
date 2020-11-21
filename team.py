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