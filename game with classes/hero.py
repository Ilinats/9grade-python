import time
import random

class Character:
    def __init__(self, name, health):
        self._name = name
        self._health = health
        self._max_health = health
        
    def get_health(self):
        print(str(self._health))
    
    def is_alive(self):
        if self._health:
            return True
        return False
        
    def take_healing(self, healing_points):
        if self._health + healing_points > self._max_health or self._health <= 0:
            return False
        
        self._health += healing_points
        return True
        
    def take_damage(self, damage_points):
        if self._health < damage_points:
            self._health = 0
        else:
            self._health = self._health - damage_points


class Hero(Character):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.__nickname = nickname
        
    def name_print(self):
        print(self._name + ' the ' + self.__nickname)
        
        
class Orc(Character):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__berserk_factor = berserk_factor
        
        if self.__berserk_factor > 2:
            self.__berserk_factor = 2
        elif self.__berserk_factor < 1:
            self.__berserk_factor = 1
            
    def check_berserk_factor(self):
        return int(self.__berserk_factor)


def play(hero, orc):
    while(hero.is_alive() and orc.is_alive()):
        time.sleep(random.random() + 0.5)
        
        match ((int)(random.randrange(0, 4))):
            case 0:
                # Orc punches human
                damage = random.randrange(1, 20) * orc.check_berserk_factor()
                hero.take_damage(damage)
                print("\nDamage taken by hero: " + str(damage))
                print("Hero health: ", end = "")
                hero.get_health()
                print("Orc health: ", end = "")
                orc.get_health()
                
            case 1:
                # Human punches orc
                damage = random.randrange(1, 20)
                orc.take_damage(damage)
                print("\nDamage taken by orc: " + str(damage))
                print("Hero health: ", end = "")
                hero.get_health()
                print("Orc health: ", end = "")
                orc.get_health()
                
            case 2:
                # human takes healing
                health = random.randrange(1, 20)
                hero.take_healing(health)
                print("\nHealing taken by hero: " + str(health))
                print("Hero health: ", end = "")
                hero.get_health()
                print("Orc health: ", end = "")
                orc.get_health()
                
            case 3:
                # orc takes healing
                health = random.randrange(1, 20)
                orc.take_healing(health)
                print("\nHealing taken by orc: " + str(health))
                print("Hero health: ", end = "")
                hero.get_health()
                print("Orc health: ", end = "")
                orc.get_health()


h = Hero("Bron", 50, "DragonSlayer")
o = Orc("Johny", 200, 2)
play(h, o)