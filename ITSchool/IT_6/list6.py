temp = [33, 22, 34, 0, 21, 22, 0]
to_remove = 22

print (temp)

print(to_remove, "apare de" , temp.count(to_remove), "ori")

if 0 in temp:
    print("S-a produs inghet")
    if temp.count(0)>1:
        print("s-a produs de mai multe ori")

temp1 = temp.copy()

temp1.reverse()
print(temp1)


print('temp max', max(temp))
print("temp min", min(temp))