# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:38:38 2020

@author: kimvd
"""

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess an number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
            
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')

guess(10)