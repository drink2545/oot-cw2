from weapon import *
class Character():
    def __init__(self):
        self.hp = 100
        if self.weapon == ' ':
            self.weapon = fist()
            print('in')
    def attack(self):
        return self.weapon.use()
    def take_dmg(self, dmg):
        self.hp -= dmg
    def set_weapon(self, weapon):
        if isinstance(weapon, weaponBehavior):
            self.weapon = weapon
            print(f'equip {self.weapon.name}')

class Knight(Character):
    def __init__(self):
        self.name = 'King'
        self.hp = 1000
        self.weapon = sword()
    def attack(self):
        return self.weapon.use() * 2.0
    def take_dmg(self, dmg):
        self.hp -= 0.3*dmg
        if self.hp < 0:
            return False


class King(Character):
    def __init__(self):
        self.name = 'King'
        self.hp = 200
        self.weapon = fist()
    def take_dmg(self, dmg):
        self.hp -= 0.2*dmg

class Troll(Character):
    def __init__(self):
        self.name = 'Troll'
        self.hp = 200
        self.weapon = axe()

class Ghost(Character):
    def __init__(self):
        self.name = 'Ghost'
        self.hp = 500
        self.weapon = fist()

class God(Character):
    def __init__(self):
        self.name = 'God'
        self.hp = 60000
        self.weapon = fist()
    