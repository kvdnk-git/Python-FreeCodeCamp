# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:29:07 2020

@author: kimvd
"""

# string concatentation
# suppose we want to create a string that says "subscribe to ___ "

# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to "+ youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")


matlib = f"Computer programming is so {adj}! \
    It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    
    
print(matlib)
