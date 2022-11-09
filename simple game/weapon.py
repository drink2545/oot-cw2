class weaponBehavior():
    def use(self):
        raise NotImplementedError

class fist(weaponBehavior):
    def __init__(self):
        self.name = 'fist'
    def use(self):
        # print('punch -10hp')
        return 10

class sword(weaponBehavior):
    def __init__(self):
        self.name = 'sword'
    def use(self):
        # print('sword slash -100hp')
        return 100

class knife(weaponBehavior):
    def __init__(self):
        self.name = 'knife'
    def use(self):
        # print('knife throwing -30hp')
        return 30

class axe(weaponBehavior):
    def __init__(self):
        self.name = 'axe'
    def use(self):
        # print('axe slash -50hp')
        return 50