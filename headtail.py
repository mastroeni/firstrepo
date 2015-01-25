import random
from collections import Counter


def headsgame(number):
    heads = 0
    tails = 0
    for x in range(0,number):
        print("Attempt number: ", x)
        possibilites = ('head', 'tail')
        draw = random.choice(possibilites)
        print (draw)
        if draw == 'tail':
            heads += 1
        else:
            tails += 1
        print( 'Tails: ', tails)
        print('Heads:' , heads)


print(headsgame(5))

__author__ = 'XYZ'
