'''
Created on 30/10/2012

@author: Toby
'''
#print("Hello Python!")

def BuyBread():
    print("Buying Bread...")
    return "Bread"   
def BuyButter():
    print("Buying Butter...")
    return "Butter"
def BuyJam():
    print ("Buying Jam...")
    return "Jam"

Food = []

Food.append( BuyBread() )
Food.append( BuyButter() )
Food.append( BuyJam() )

print(Food)

#BuyBread()
#BuyButter()
#BuyJam()