'''
Created on 15/11/2012

@author: Toby
'''
milk_price = input("Enter a number:")
if milk_price <= 1.25:
        print("Buy two cartons of milk, they're on sale")
elif milk_price <= 2.00:
        print("Buy one carton of milk, prices are normal")
elif milk_price > 2.00:
        print("Go somewhere else! Milk costs too much here")