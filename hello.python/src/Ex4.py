'''
Created on 15/11/2012

@author: Toby
'''
import time

i = input("Enter countdown : ")
while i > 0:
    print("Lift off in:")
    print(i)
    time.sleep(1)
    i=i - 1  

if i == 0:
    print("Lift off!")