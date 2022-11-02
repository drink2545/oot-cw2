from appliances import *
class command():
    def execute(self):
        raise NotImplementedError
    def undo(self):
        raise NotImplementedError

class Nocommand(command):
    def execute(self):
        pass
    def undo(self):
        pass

class Light_on_command(command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class Light_off_command(command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

class AC_on_command(command):
    def __init__(self, ac):
        self.ac = ac
    def execute(self):
        self.ac.turn_on()
    def undo(self):
        self.ac.turn_off()

class AC_off_command(command):
    def __init__(self, ac):
        self.ac = ac
    def execute(self):
        self.ac.turn_off()
    def undo(self):
        self.ac.turn_on()

class tv_on_command(command):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.turn_on()
    def undo(self):
        self.tv.turn_off()

class tv_off_command(command):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.turn_off()
    def undo(self):
        self.tv.turn_on()

class bothAcAndLightOn(command):
    def __init__(self, ac, light):
        self.ac = ac
        self.light = light

    def execute(self):
        self.ac.turn_on()
        self.light.on()
    
    def undo(self):
        self.ac.turn_off()
        self.light.off()

class bothAcAndLightOff(command):
    def __init__(self, ac, light):
        self.ac = ac
        self.light = light

    def execute(self):
        self.ac.turn_off()
        self.light.off()
    
    def undo(self):
        self.ac.turn_on()
        self.light.on()

class allOn(command):
    def __init__(self, light, ac, tv):
        self.light = light
        self.ac = ac
        self.tv = tv
    
    def execute(self):
        self.light.on()
        self.ac.turn_on()
        self.tv.turn_on()
    
    def undo(self):
        self.light.off()
        self.ac.turn_off()
        self.tv.turn_off()

class allOff(command):
    def __init__(self, light, ac, tv):
        self.light = light
        self.ac = ac
        self.tv = tv
    
    def execute(self):
        self.light.off()
        self.ac.turn_off()
        self.tv.turn_off()
    
    def undo(self):
        self.light.on()
        self.ac.turn_on()
        self.tv.turn_on()