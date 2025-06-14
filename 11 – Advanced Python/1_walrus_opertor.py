if(n := len([1,2,3,4,5]))>3:
    print(f"list is long {n}")  #(:=)use walrus opertor for 2 work in one line


#Ex-2

while (data := input("Enter: ")) != "quit":
    print(f"You typed: {data}")
