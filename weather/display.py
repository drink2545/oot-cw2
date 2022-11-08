from weather_data import *

class display():
    def __init__(self):
        raise NotImplementedError

    def update(self, args):
        raise NotImplementedError
    
    def render_display(self):
        raise NotImplementedError

class current(display):
    
    def __init__(self, weatherdata):
        self.weatherdata = weatherdata
        weatherdata.reg_obs(self)
        self.maxtemp = 0.0

    def update(self,  temp, pressure, humidity):
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        if self.temp > self.maxtemp:
            self.maxtemp = self.temp
        self.render_display()
{(a, p({a,b}, {c})), p({c}, {d,e}), (iL, a), (e, oL)}
    def render_display(self):
        print(f'current temperature: {self.temp}')
        print(f'max temperature: {self.maxtemp}\n')