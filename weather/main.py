from re import L
from weather_data import *
from display import *
import time

def main():
    x = weatherdata()
    current_display = current(x)
    x.measure_change()
    time.sleep(2)
    x.measure_change()
    time.sleep(2)
    x.measure_change()
if __name__ == "__main__":
  main()