try:
     a=int(input("enter:"))

     print(a)

except ValueError as v:   
     print("check")
     print(v)

except Exception as e:
     print(e)

print("OK test")