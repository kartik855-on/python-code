i = 1

while(i<51):
    print(i)
    i +=1

print("break loop")

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

print("continue")

i = 0
while i < 5:
    i += 1
    if i == 3:       #skip the velue 3
        continue
    print(i)