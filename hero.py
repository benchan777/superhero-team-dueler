import random
from ability import Ability
from armor import Armor
from weapon import Weapon

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
      self.deaths = 0
      self.kills = 0

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
        self.add_kill(1)
        opponent.add_death(1)
        print(f"{self.name} won!")
      else:
        opponent.add_kill(1)
        self.add_death(1)
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

  def add_weapon(self, weapon):
    ''' Add weapon to self.abilities '''
    self.abilities.append(weapon)

  def add_kill(self, num_kills):
    ''' Update self.kills by num_kills amount. '''
    self.kills += num_kills
    return self.kills

  def add_death(self, num_deaths):
    ''' Update deaths with num_deaths. '''
    self.deaths += num_deaths
    return self.deaths

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())