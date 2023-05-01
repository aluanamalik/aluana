import time
import random
from math import sqrt
integer = int(input())
rnd = random.randint(1,3000) / 1000
screen_rnd = rnd * 1000
time.sleep(rnd)

print(f"Square root of {integer} after {int(screen_rnd)} miliseconds is {sqrt(integer)}")
