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
            freq = input("Looser type curls and coily curls can be lathered anywhere from two to four times a week, with time intervals of 1 day to 2 days in between those for the hair to readjust before the next wash!\nWashing your hair too often results in a tighter and more dry scalp and frizzy hair, which is not our motto! On the contrary, washing hair less often can lead to a greasy feeling at the scalp, and significantly brittle hair. Moral of the story is, listen to your scalp!\nWe want to know how often you wash your hair so that if we believe you may need to adjust this, we can provide a reccomendation!\nPlease enter an integer number of days you wait until your next hair wash: ")
        freq = int(freq)
        conditioner = (input("\nDo you use conditioner? Please enter the number option that describes you best:\n1. Every hair wash\n2. Sometimes\n3. Never\n(enter 'w' to ask why we need this)\n"))
        if conditioner == 'w':
            conditioner = input("Having absolutely gorgeous ringlets can come with a price - if the curls are very coily, the harder it is for moisture to penetrate to the scalp.\nThe shape of the ringlets can be altered using chemical methods such as “Keratin” straightening treatments, heat styling, pollution, and especially hard water!\nPlease enter an integer based on the above that describes your conditioning habits! ")
        conditioner = int(conditioner)
        thickness = input("\nOn a scale of 1 to 10, how thick is your hair? 1 is for very thin, 10 is for very thick (enter 'w' to ask why we need this): ")
        if thickness == 'w':
            thickness = input("Here thickness is defined by how well you can see through the scalp. Thicker hair tends to be harder to see through and the opposite goes for thin hair. Pluck a strand of hair from the crown of your scalp and compare it to a standard sewing thread. If it is thicker, you hair is on the higher end and if it is thinner, it is classified on the lower end!\nPlease enter how thick your hair is on a scale of 1 to 10: ")
        thickness = int(thickness)
        
        hairlen = input("\nHow long is your hair? Please enter the number option that describes you best:\n1. Below waist\n2. Mid-back\n3. Below shoulders\n4. Above shoulders\n5. Pixie cut\n(enter 'w' to ask why we need this)\n")
        if hairlen == 'w':
            hairlen = input("Curly manes can have a variety of different lengths, anywhere from pixie cuts to short and cropped, or even go up to your shoulders. We’ve classified 5 different hair lengths, from 5 being a pixie cut to 1 being mid or lower back! Combining this along with how frequently you wash your hair we may give you water conservation tips!\nPlease enter the integer based on the above that describes your hair length!: ")
        hairlen = int(hairlen)
        
        dryness = input("\nDo you tend to have a dry scalp? Enter 0 if no and 1 if yes (enter 'w' to ask why we need this): ")
        if dryness == 'w':
            dryness = input("A dry scalp can be the result of hair losing an excess amount of moisture, which can result in itching or flaking. Some hair shampoos that contain sulphates are infamously known to dry out your scalp.\nThere can be underlying conditions associated with a dry scalp such as psoriasis, or seborrheic dermatitis which result in chronic itching. Please consult your doctor or a hair professional before making any assessment!\nPlease enter 0 if you tend to not have a dry scalp and a 1 if you tend to have a dry scalp: ")
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
