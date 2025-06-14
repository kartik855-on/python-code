class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)




class vactor:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        result=vactor(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    def __mul__(self,other):
        result=vactor(self.x*other.x,self.y*other.y,self.z*other.z)
        return result
    def __str__(self):
        return(f"{self.x} {self.y} {self.z}")

v1=vactor(1,2,3)
v2=vactor(1,2,3)
v3=vactor(5,4,3)

print(v1*v2)