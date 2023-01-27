########
#import modules
#######

########
#define functions
#######
import os
import time

def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 1
    if minutes >= 30:
        gameover()
    else:
        print("She will be in shoping centre", 30 - minutes, "minutes")

def gameover():
    if minutes <= 0:
        print("You didn't make it,Now you're the one whose late and your best friend is waiting for you at the elevator. Game over! ")

    elif minutes == 0:
        print("You didn't make it,Now you're the one whose late and your best friend is waiting for you at the elevator. Game over! ")
    else:
        print("\nok, better luck next time!")

def start():
    print("Welcome! You have a meeting with your best friend in Pentagon city near elevetors, but she is going to be late and now you have extra 30 minets. Do you want go somewhere?")

    choice = input()
    if choice.lower() == "yes":
        print("You are near entrance")
        move = input("\nWhere would you like to go? Say one of these choices:\n Victoria's Secret\n Lego store\n Sephora\n Macy's\n")
        if move.lower() == "victoria's secret":
            VictoriasSecret()
        elif move.lower() == "lego store":
            Legostore()
        elif move.lower() == "sephora":
            Sephora()
        elif move.lower() == "macy's":
            Macys()
        else:
            print("You can not do that")
        
    else:
        print("You will get bored. Do you want go somewhere?")

def VictoriasSecret():
    check_time()
    print("You are in Victoria's Secret. Assistan come to you and ask if you need help. Do you need help or not?")
    choice_1 = input()
    if choice_1.lower()== "yes":
        print("The assistant was really helpful and you finaly found a perfume that you really like, but the line is so long. Do you want to buy it now or come back later with your bestie? ")
        choice_2 = input()
        if choice_2.lower() == "i want to buy it now":
            print("You spent 20 minutes in a line. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
        elif choice_2.lower() == "i want to come back later with my bestie":
            print("You go back and meet with your best friend near elevetor. You won! '(0_0)'")
        else:
            print("I dont know what you talk abou! Try again")
            VictoriasSecret()
    elif choice_1.lower() == "no":
        print("You spent 35 minutes trying to find perfume to your liking but couldn't find any. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
    else: 
        #TODO: what should happen if they type something else?
        pass


def Sephora():
    check_time()
    print("You are in Sephora. Assistan come to you and ask if you need help. Do you need help or not?")
    choice_1 = input()
    if choice_1.lower() == "yes":
        print("The assistant was really helpful and you finaly found a perfume that you really like, but the line is so long. Do you want to buy it now or come back later with your bestie? ")
        choice_2 = input()
        if choice_2.lower() == "i want to buy it now":
            print("You spent 20 minutes in a line. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
        elif choice_2.lower() == "i want to come back later with my bestie":
            print("You go back and meet with your best friend near elevetor. You won! '(0_0)'")
        else:
            print("I dont know what you talk abou! Try again")
        Sephora()
    elif choice_1.lower() == "no":
        print("You spent 35 minutes trying to find perfume to your liking but couldn't find any. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
    else: 
        #TODO: what should happen if they type something else?
        pass


def Legostore():
    check_time()
    print("You are in Lego store. Assistan come to you and ask if you need help. Do you need help or not?")
    choice_1 = input()
    if choice_1.lower() == "yes":
        print("The assistant was really helpful and you finaly found a lego that you really like, but the line is so long. Do you want to buy it now or come back later with your bestie? ")
        choice_2 = input()
        if choice_2.lower() == "i want to buy it now":
            print("You spent 20 minutes in a line. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
        elif choice_2.lower() == "i want to come back later with my bestie":
            print("You go back and meet with your best friend near elevetor. You won! '(0_0)'")
        else:
            print("I dont know what you talk abou! Try again")
            Legostore()
    elif choice_1.lower() == "no":
        print("You spent 35 minutes trying to find lego to your liking but couldn't find any. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
    else: 
        #TODO: what should happen if they type something else?
        pass

def Macys():
    check_time()
    print("You are in Macy's. Assistan come to you and ask if you need help. Do you need help or not?")
    choice_1 = input()
    if choice_1.lower() == "yes":
        print("The assistant wasn't really helpful and you didn't find a dress that you like. Do you want search more or come back later with your bestie? ")
        choice_2 = input()
        if choice_2.lower() == "i want want search more":
            print("You spent 20 minutes trying to search more. Now you're the one whose late and your best friend is waiting for you at the elevator. Game over!")
        elif choice_2.lower() == "i want to come back later with my bestie":
            print("You go back and meet with your best friend near elevetor. You won! '(0_0)'")
        else:
            print("I dont know what you talk abou! Try again")
            Macys()
    elif choice_1.lower() == "no":
        print("You go back and meet with your best friend near elevetor. You won! '(0_0)'")
    else: 
        #TODO: what should happen if they type something else?
        pass




########
#main
#######
#TODO: Add some global variables

minutes = 0
start()