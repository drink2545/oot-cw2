from beverage import beverage
class condiment(beverage):
    def __init__(self, beverage):
        self.beverage = beverage
    def get_descrip(self):
        raise NotImplementedError

class milk(condiment):
    
    def get_descrip(self):
        return self.beverage.get_descrip() + ', Milk'
    
    def cost(self):
        return 0.10 + self.beverage.cost()

class mocha(condiment):
    
    def get_descrip(self):
        return self.beverage.get_descrip() + ', Chocolate'
    
    def cost(self):
        return 0.20 + self.beverage.cost()

class whip(condiment):
    
    def get_descrip(self):
        return self.beverage.get_descrip() + ', Whipped Cream'
    
    def cost(self):
        return 0.10 + self.beverage.cost()
    