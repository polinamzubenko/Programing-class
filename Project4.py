import random #Importing the random method
import time #Importing the time method

print("This small program will help you find out\nwhat the chance of one or another number on the die\nfor a certain number of rolls")
time.sleep(3) 

totali = int(input("Enter the desired number of cube tosses: ")) #Total number of die rolls
time.sleep(1)
numi = int(input("Enter the number you want to know the number of rolls: ")) #The number we are interested in
time.sleep(1)
numil = int(input("Enter the number of numbers on the cube: ")) #Number of numbers on the cube
time.sleep(4)
totalnum = 0 #Total number of die rolls
zero = 0 #The number we are interested in
while zero < totali: 
    one = random.randint(1, numil) #Find a random number
    if one == numi:
        zero = zero + 1 #Total number of die rolls
        totalnum = totalnum + 1 #The number we are interested in
    elif one != numi:
        zero = zero + 1 #Total number of die rolls
print("Percentage drop of the number", numi, "on the die:", round(totalnum/totali*100, 2),"%") #Result

