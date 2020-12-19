###
#import random

#U_choice = (input("What is your choice among r, p, or s? "))
#I_choice=random.randrange("r","p","s")
#if U_choice ==r and I_choice==r:
 #   print("Its a smashing tie")

#elif U_choice ==r and I_choice==p:
#   print('I chose p.')

user_play="y"

start_number = 0 

while user_play =="y":
    number=input("What is your number?")
    x=int(number)
    for x in range(start_number,x+start_number):
        print (x)
    start_number=start_number+x
    user_play=input("Do you still want to play?(y/n)")





