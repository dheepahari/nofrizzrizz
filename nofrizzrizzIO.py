# -*- coding: utf-8 -*-
"""
@author: 18607
"""


import sys
import os


class nofrizzrizz():
    def __init__ (self) -> None:
        self.test = 0
    
    
    def test_func(self, a, b):
        return (a + b)
    
    def hairquiz(self):
        #val = input("Enter your value: ")
        #val2 = input("Enter your other value: ")
        #return int(val) + int(val2)
        freq = input("How many days do you wait until your next hair wash? Please enter an integer (enter 'w' to ask why we need this): ")
        if freq == 'w':
            freq = input("The number of times you wash your hair is dependent on ___! Please enter an integer number of days you wait until your next hair wash: ")
        freq = int(freq)
        conditioner = (input("\nDo you use conditioner? Please enter the number option that describes you best:\n1. Every hair wash\n2. Sometimes\n3. Never\n(enter 'w' to ask why we need this)\n"))
        if conditioner == 'w':
            conditioner = input("Conditioner helps with ___ but should be used when ___ depending on ___! Please enter an integer based on the above that describes your conditioning habits! ")
        conditioner = int(conditioner)
        thickness = input("\nOn a scale of 1 to 10, how thick is your hair? 1 is for very thin, 10 is for very thick (enter 'w' to ask why we need this): ")
        if thickness == 'w':
            thickness = input("_____! Please enter how thick your hair is on a scale of 1 to 10: ")
        thickness = int(thickness)
        
        hairlen = input("\nHow long is your hair? Please enter the number option that describes you best:\n1. Below waist\n2. Mid-back\n3. Below shoulders\n4. Above shoulders\n5. Pixie cut\n(enter 'w' to ask why we need this)\n")
        if hairlen == 'w':
            hairlen = input("_____! Please enter the integer based on the above that describes your hair length!: ")
        hairlen = int(hairlen)
        
        dryness = input("\nDo you tend to have a dry scalp? Enter 0 if no and 1 if yes (enter 'w' to ask why we need this): ")
        if dryness == 'w':
            dryness = input("___! Please enter 0 if you tend to not have a dry scalp and a 1 if you tend to have a dry scalp: ")
        dryness = int(dryness)
        
        budget = input("\nAre you on a budget? Please enter the number option that describes you best:\n1. No, I am not\n2. Yes, I'm on a budget\n3. I can't spend any money\n(enter 'w' to ask why we need this)\n")
        if budget == 'w':
            budget = input("Part of what we'll be doing is reccomending products to you based on your hair as well as your budget! We would like to make sure that our suggestions are affordable for your lifestyle!\nPlease enter the number option that best describes your budget: ")
        budget = int(budget)
        
        if budget > 1:
            bstr = ""
        else:
            bstr = "not "
        
        return f"The user washes their hair every {freq} days and is {bstr}on a budget."


if __name__ == "__main__":
    initcurls = nofrizzrizz()
    if sys.argv[1] == "-t":
        print(initcurls.test_func(1, 2))
    elif sys.argv[1] == "-q":
        print(initcurls.hairquiz())
