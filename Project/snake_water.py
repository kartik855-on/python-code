import random
'''
 1 - snake
-1 - water
 0 - gun
'''
computer = random.choice([-1,0,1])
youstr= input("enter you choice: ")
youDict={ "s": 1, "w": -1, "g": 0 }
revDict={1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f"you choice {revDict[you]}\ncomputer choice {revDict[computer]}")
if(computer==you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you Lose!")

    elif(computer == 1 and you == -1):
        print("you Lose!")

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer == 0 and you == -1):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you Lose!")

    else:("something went rong!")