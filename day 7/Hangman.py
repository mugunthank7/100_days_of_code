from numpy.matlib import rand
import random

from numpy.random import gumbel

word_list = ["naana" ,"banana" ,"apple" ,"kabali"]

#get input from the user and test if its there or not
chosen_word = random.choice(word_list)
blanks = [0] *len(chosen_word)
print(blanks)
decision= "Wrong"
lives=5
guess = input(" Guess a letter ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
print(decision)






