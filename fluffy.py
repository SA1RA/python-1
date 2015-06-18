
import colors as c
import random as r
import random


""" The pink fluffy unicorn quiz module."""


print(c.clear)
print(c.base3 + 'samuel lucas is not responsible for anything in this quiz.' + c.reset)
print(c.yellow + 'welcome to the quiz game for unicorn hunters.' + c.reset)


def q1():
    print(c.red  + 'What is the color of the pink fluffy unicorn?')
    answer == input('> ').strip().lower()
    if answer.startswith("pink"):
        return True
    else:
        return False

def q2():
    print(c.red + 'What is the pink fluffy unicorn dancing on?')
    answer == input('> ').strip().lower()
    if answer.startswith("rainbow"):
        return True
    else:
        return False

def q3():
    print(c.red + 'How do we describe the pink fluffy unicorns fur?')
    answer == input('> ').strip().lower()
    if answer.startswith("smile"):
        return True
    else:
        return False

questions = [q1,q2,q3]
