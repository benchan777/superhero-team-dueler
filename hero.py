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

  def defend(self, damage_amt):
    ''' Calculate the total block amount from all armor blocks.
        return: total_block:Int
    '''
    block_amount = 0
    for armor in self.armors:
      block_amount += armor.block()
    total_block = damage_amt - block_amount
    return total_block

  def take_damage(self, damage):
    ''' Updates self.current_health to reflect the damage minus the defense.
    '''
    damage_taken = damage - self.defend(damage)
    self.current_health -= damage_taken
    return self.current_health


if __name__ == "__main__":
  hero = Hero("Grace Hopper", 200)
  shield = Armor("Shield", 50)
  hero.add_armors(shield)
  hero.take_damage(50)
  print(hero.current_health)