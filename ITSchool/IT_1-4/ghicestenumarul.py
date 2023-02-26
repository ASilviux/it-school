from random import randint
ran_nr= randint(1,99)
print(ran_nr)

print("Incepe jocul")
print("alege un numar intre 1 si 99")
choice =input("Select a number " )

while (choice != ran_nr):
    print ("is not the correct number")
    print("Guess again")
    choice= input("Select a number: " )