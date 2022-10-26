class beverage():
    def __init__(self):
        self.descrip = 'unknow'
    def get_descrip(self):
        return self.descrip
    def cost(self):
        raise NotImplementedError

class darkRoast(beverage):
    def __init__(self):
        self.descrip = 'Dark Roast'
    def cost(self):
        return 0.99

class decaf(beverage):
    def __init__(self):
        self.descrip = 'Decaf'
    def cost(self):
        return 1.05

class espresso(beverage):
    def __init__(self):
        self.descrip = 'Espresso'
    def cost(self):
        return 1.99

