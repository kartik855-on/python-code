class employ:
  a=1
class coder(employ):
  b=2
class manager(coder):
  c=3

x=manager()
print(x.a,x.b,x.c)