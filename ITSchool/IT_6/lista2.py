user_ids = [324, 345, 536, 64]

for i in user_ids:
    print(i)

user_idx = range(len(user_ids))

for i in user_idx:
    print("Index" , i , "Valoare", user_ids[i])

for i in range(len(user_ids)):
        print("Index" , i , "Valoare", user_ids[i])


for i in enumerate(user_ids):
         print("Index" , i[0] , "Valoare", i[1])
