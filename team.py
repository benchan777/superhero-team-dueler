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