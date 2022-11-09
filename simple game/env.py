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
        # print(f'\n{self.enemy.name} HP: {self.enemy.hp}')
        if action == 'attack':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(dmg_from_x)

            dmg = self.hero.attack()
            self.enemy.take_dmg(dmg)
            self.attack_count += 1
        
        elif action == 'defend':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(0.1* dmg_from_x)
            print(f'Hero HP: {self.hero.hp}')
        
        if self.enemy.hp < 0:
            print(f'Attack {self.attack_count} times')
            self.attack_count = 0
            print(f'{self.enemy.name} is dead\n')
            self.kill += 1
            self.enemy = random.choice([Troll(),Ghost()])

            return random.choice([sword(), knife(), axe(), adapterLightSaber(), adapterLaserGun(), adapterElectricShotgun])
        else:
            return None

if __name__ == '__main__':
    cha = random.choice([Knight(), King()])
    # w = random.choice([sword(), knife(), axe(), adapterLightSaber(), adapterLaserGun(), adapterElectricShotgun])
    w = adaptertest()
    env = Env(cha)
    env = Env(cha)

    while True:
        # drop = env.step(random.choice(['attack', 'defend']))
        drop = env.step('attack')
        # if drop:
        #     cha.set_weapon(drop)
        if cha.hp < 0:
            print('Hero die')
            break

    print(f'Hero kill {env.kill} enemy.')