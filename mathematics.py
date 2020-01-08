import math

cos = math.cos(math.pi/4)
print(f'math.cos(math.pi/4) => {cos}')
log = math.log(1024,2)
print(f'math.log(1024,2) => {log}')

import random
choiced = random.choice(['apple','pear','banana'])
print(f'random.choice(["apple","pear","banana"] => {choiced}')

samples = random.sample(range(100), 10)
print(f'random.sample(range(100), 10) => {samples}')


rand = random.random()
print(f'random.random() => {rand}')
rand = random.randrange(5)
print(f'random.random(5) => {rand}')