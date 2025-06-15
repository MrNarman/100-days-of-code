import random

heads = 1

roll = random.randint(1, 2)
if roll == heads:
    print('HEADS')
else:
    print('TAILS')