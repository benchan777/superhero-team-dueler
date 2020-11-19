import random

class Hero:
  def __init__(self, name, starting_health=100):
      '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
      '''
      self.name = name
      self.starting_health = starting_health
      self.current_health = starting_health

  def fight(self, opponent):
      opponent_list = []
      opponent_list.append(self.name)
      opponent_list.append(opponent.name)
      print(f"{random.choice(opponent_list)} won!")

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2)