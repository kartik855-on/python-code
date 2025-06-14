class employ:
    def __init__(self):
        print("constroter of employ")
    a=1

class programer(employ):
    def __init__(self):
        super().__init__()
        print("constroctor of programer")
    b=2

class manger(programer):
    def __init__(self):
        super().__init__()
        print("constrator of manger")
    c=3

x=manger()
print(x.a,x.b,x.c)
