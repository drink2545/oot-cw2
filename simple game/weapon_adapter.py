from space_weapon import *
from weapon import *

# class adapterLaserGun(weaponBehavior):
#     def __init__(self) -> None:
#         self.name = 'Laser Gun'
#         self.laser_gun = LaserGun()

#     def use(self):
#         dmg = self.laser_gun.shoot()
#         if self.laser_gun.energy < 0:
#             self.laser_gun.reload()

#         return dmg

# class adapterElectricShotgun(weaponBehavior):
#     def __init__(self) -> None:
#         self.name = 'Electric Shotgun'
#         self.laser_gun = ElectricShotgun()

#     def use(self):
#         dmg = self.laser_gun.shoot()
#         if self.laser_gun.energy < 0:
#             self.laser_gun.reload()

#         return dmg

# class adapterLightSaber(weaponBehavior):
#     def __init__(self) -> None:
#         self.name = 'Light saber'
#         self.light_saber = LightSaber()
    
#     def use(self):
#         dmg = self.light_saber.slash()
#         if self.light_saber.energy < 0:
#             self.light_saber.charge()
#         return dmg

class adapterLaserGun(weaponBehavior, LaserGun):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Laser Gun'
    def use(self):
        dmg = self.shoot()
        if self.energy < 0:
            self.reload()
        return dmg

class adapterElectricShotgun(weaponBehavior, ElectricShotgun):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Electric Shotgun'
    def use(self):
        dmg = self.shoot()
        if self.energy < 0:
            self.reload()
        return dmg

class adapterLightSaber(weaponBehavior, LightSaber):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Light Saber'
    def use(self):
        dmg = self.shoot()
        if self.energy < 0:
            self.reload()
        return dmg
