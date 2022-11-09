from character import *
from weapon import *
import random

class Env():
    def __init__(self, hero):

        self.hero = hero
        self.enemy = Troll()
        self.kill = 0
    
    def step(self, action):
        if action == 'attack':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(dmg_from_x)

            dmg = self.hero.attack()
            self.enemy.take_dmg(dmg)
        
        elif action == 'defend':
            dmg_from_x = self.enemy.attack()
            self.hero.take_dmg(0.1* dmg_from_x)
        
        if self.enemy.hp < 0:
            print(f'{self.enemy.name} is dead')
            self.kill += 1

            self.enemy = random.choice([Troll(),Ghost()])

            return random.choice([sword(), knife(), axe()])
        else:
            return None
if __name__ == '__main__':
    cha = Knight()
    w = random.choice([sword(), knife(), axe()])
    env = Env(cha)

    for i in range(100):
        drop = env.step('attack')
        if drop:
            cha.set_weapon(drop)
    
    print(f'Hero kill {env.kill} enemy.')