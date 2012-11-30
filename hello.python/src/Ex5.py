'''
Created on 15/11/2012

@author: Toby
'''
import time
for i in range(10, 0, -1):
    print("T-minus: ")
    print(i)
    time.sleep(1)

if i == 1:
    print("Lift off!")