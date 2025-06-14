import random
n=random.randint(1,100)
a=-1
guesses=1

while(a!=n):
    a=int(input("enter you guesses number: "))
    if(a>n):
        print("lower number plese")
        guesses+=1
    elif(a<n):
        print("higher number plese")
        guesses+=1

print(f"you have have guessed nuber {n} correct in guesses {guesses} attempts")