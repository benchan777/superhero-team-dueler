import random
from ability import Ability
from armor import Armor

class Hero:
  def __init__(self, name, starting_health=100):
      '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
      '''
      self.abilities = list()
      self.armors = list()
      self.name = name
      self.starting_health = starting_health
      self.current_health = starting_health

  def fight(self, opponent):
      opponent_list = []
      opponent_list.append(self.name)
      opponent_list.append(opponent.name)
      print(f"{random.choice(opponent_list)} won!")

  def add_ability(self, ability):
    ''' Add ability to abilities list '''
    self.abilities.append(ability)

  def add_armors(self, armor):
    ''' Add armor to self.armors
        Armor: Armor Object
    '''
    self.armors.append(armor)

  def attack(self):
    ''' Calculate the total damage from all ability attacks.
        return: total_damage:Int
    '''
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def defend(self):
    ''' Calculate the total block amount from all armor blocks.
        return: total_block:Int
    '''
    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
    return total_block

  def take_damage(self):
    ''' Updates self.current_health to reflect the damage minus the defense.
    '''
    

if __name__ == "__main__":
  ability = Ability("Great Debugging", 50)
  another_ability = Ability("Smarty Pants", 90)
  armor = Armor("Big Shield", 30)
  armor2 = Armor("Helmet", 10)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  hero.add_ability(another_ability)
  hero.add_armors(armor)
  hero.add_armors(armor2)
  print(hero.attack())
  print(hero.defend())