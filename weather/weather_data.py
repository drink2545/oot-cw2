import numpy as np

class subject():
    def __init__(self):
        self.observers = []
    def reg_obs(self,obs):
        raise NotImplementedError
    def remove_obs(self,obs):
        raise NotImplementedError
    def not_obs(self, temp, pressure, humidity):
        raise NotImplementedError

class weatherdata(subject):
    def __init__(self):
        super().__init__()
    def reg_obs(self, obs):
        self.observers.append(obs)
    def remove_obs(self, obs):
        self.observers.remove(obs)
    def not_obs(self, temp, pressure, humidity):
        for obs in self.observers:
            obs.update(temp,pressure,humidity)

    def get_temp(self):
        return 35.0 + 8.0 * np.random.randn()
    def get_pressure(self):
        return 100.0 + 20.0 * np.random.randn()
    def get_humidity(self):
        return 70.0 + 10.0 * np.random.randn()

    def measure_change(self):
        temp = self.get_temp()
        pressure = self.get_pressure()
        humidity = self.get_humidity()

        self.not_obs(temp,pressure,humidity)
