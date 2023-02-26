temp = [33, 22, 34, 21, 22, 0]

print(temp)

temp.remove(22) #prima aparatie
print(temp)

to_remove = 22
while to_remove in temp:
    temp.remove(to_remove)

print(temp)

if 0 in temp:
    print("S-a produs inghet")