class spaceWeaponBehavior():
    def shoot(self):
        raise NotImplementedError
    
    def reload(self):
        raise NotImplementedError

class LaserGun(spaceWeaponBehavior):
    def __init__(self) -> None:
        self.energy = 100
    
    def shoot(self):
        print('shoot')
        self.energy -= 10

        if self.energy > 0:
            return 1000
        else:
            return 0

    def reload(self):
        print('reload')
        self.energy = 100

class ElectricShotgun(spaceWeaponBehavior):
    def __init__(self) -> None:
        self.energy = 100
    
    def shoot(self):
        print('shoot')
        self.energy -= 50

        if self.energy > 0:
            return 1000
        else:
            return 0

    def reload(self):
        print('reload')
        self.energy = 100

class LightSaber(spaceWeaponBehavior):
    def __init__(self) -> None:
        self.energy = 9999
    
    def slash(self):
        self.energy -= 1
        if self.energy > 0:
            return 1000
        else:
            return 0

    def charge(self):
        print('Charging')
        self.energy = 9999