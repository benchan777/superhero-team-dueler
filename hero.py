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

  # def fight(self, opponent):
  #     opponent_list = []
  #     opponent_list.append(self.name)
  #     opponent_list.append(opponent.name)
  #     print(f"{random.choice(opponent_list)} won!")

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
    if not self.armors:
      total_block = 0
      return total_block
    else:
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

  def is_alive(self):
    ''' Return True or False depending on whether the hero is alive or not.
    '''
    if self.current_health <= 0:
      return "False"
    else:
      return "True"

  def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.
    '''
    if not self.abilities and opponent.abilities:
      print("Draw")
    else:
      while self.current_health and opponent.current_health > 0:
        opponent.take_damage(self.attack())
        self.take_damage(opponent.attack())

      if self.current_health > opponent.current_health:
        print(f"{self.name} won!")
      else:
        print(f"{opponent.name} won!")

        # if opponent.is_alive() == "True":
        #   break
        # else:
        #   print(f"{self.name} won!")

        # self.take_damage(opponent.attack())

        # if self.is_alive() == "True":
        #   break
        # else:
        #   print(f"{opponent.name} won!")

if __name__ == "__main__":
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 800)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2)