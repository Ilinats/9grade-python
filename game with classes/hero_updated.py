import time
import random

class Character:
    def __init__(self, name, health):
        self._name = name
        self._health = health
        self._max_health = health
        self.weapon = 0
        self.damage = 0
        self.critical = 0
        
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
            
    def has_weapon(self):
        if self.weapon:
            return True
        
        return False
        
    def equip_weapon(self, weapon):
        self.weapon = weapon.type_of_weapon()
        self.damage = weapon.damage_done()
        self.critical = weapon.critical_hit()
        
    def attack(self):
        if self.critical:
            self.damage *= 2
            
        return self.damage


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
            
    def check_berserk_factor(self):
        return int(self.__berserk_factor)
    
    def attack(self):
        if self.critical:
            self.damage *= 2
            
        return self.damage *self.__berserk_factor
    
class Weapon:
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent
        
    def critical_hit(self):
        hit = random.randint(1, 10)
        chance = self.critical_strike_percent * 10
        
        if chance == 0 or hit > chance:
            return False

        return True
    
    def damage_done(self):
        return int(self.damage)
    
    def type_of_weapon(self):
        return str(self.type)


def print_health(hero, orc):
    print("Hero health: ", end = "")
    hero.get_health()
    print("Orc health: ", end = "")
    orc.get_health()

def play(hero, orc, weapon):
    hero.equip_weapon(weapon)
    orc.equip_weapon(weapon)
    
    while(hero.is_alive() and orc.is_alive()):
        time.sleep(random.random() + 0.5)
        
        match ((int)(random.randrange(0, 4))):
            case 0:
                # Orc punches human
                damage = orc.attack()
                hero.take_damage(damage)
                print("\nDamage taken by hero: " + str(damage))
                print_health(hero, orc)
                
            case 1:
                # Human punches orc
                damage = hero.attack()
                orc.take_damage(damage)
                print("\nDamage taken by orc: " + str(damage))
                print_health(hero, orc)
                
            case 2:
                # human takes healing
                health = random.randrange(1, 20)
                hero.take_healing(health)
                print("\nHealing taken by hero: " + str(health))
                print_health(hero, orc)
                
            case 3:
                # orc takes healing
                health = random.randrange(1, 20)
                orc.take_healing(health)
                print("\nHealing taken by orc: " + str(health))
                print_health(hero, orc)


h = Hero("Bron", 50, "DragonSlayer")
o = Orc("Johny", 200, 2)
w = Weapon("axe", 10, 0.3)
play(h, o, w)