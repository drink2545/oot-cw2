from character import *
from weapon import *
from weapon_adapter import *
import random

class Env():
    def __init__(self, hero):

        self.hero = hero
        self.enemy = Troll()
        self.kill = 0
        self.attack_count = 0
    
    def step(self, action):
        
        if action == 'attack':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(dmg_from_x)

            dmg = self.hero.attack()
            self.enemy.take_dmg(dmg)
            self.attack_count += 1
            # print(f'{self.enemy.name} HP: {self.enemy.hp}')
            
        elif action == 'defend':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(0.1* dmg_from_x)
            
        
        if self.enemy.hp < 0:
            print(f'Attack {self.attack_count} times')
            self.attack_count = 0
            print(f'{self.enemy.name} is dead\n')
            self.kill += 1
            self.enemy = random.choice([Troll(),Ghost()])
            print('Hero HP: %.2f'%self.hero.hp)
            return random.choice([adapterLaserGun(), adapterElectricShotgun])
        else:
            return None

if __name__ == '__main__':
    # cha = random.choice([Knight(), King()])
    cha = Knight()
    w = random.choice([adapterLaserGun(), adapterElectricShotgun()])
    env = Env(cha)

    while True:
        drop = env.step(random.choice(['attack', 'defend']))
        # drop = env.step('attack')
        if drop:
            cha.set_weapon(drop)
        if cha.hp < 0:
            print('Hero die')
            break

    print(f'Hero kill {env.kill} enemy.')