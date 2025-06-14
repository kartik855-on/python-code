#Function with Arguments

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("kartik", "Thank you") 
print(a)


# Default Argument

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("mohit", "Thanks")
goodDay("Rohan")