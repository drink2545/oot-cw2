from beverage import *
from condiment import *

my_cup = espresso()
my_cup = milk(my_cup)

print("\nMy Order: Latte")
print(f'Description: {my_cup.get_descrip()}')
print(f'Cost: {my_cup.cost()}\n')

Mochalatte = whip(mocha(milk(espresso())))

print("My Order: Mocha Latte with whipped cream")
print(f'Description: {Mochalatte.get_descrip()}')
print(f'Cost: {Mochalatte.cost()}\n')