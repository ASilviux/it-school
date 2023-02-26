birth_year = input("what is the year of your birth: " )
current_year = input ("what is the current year: ")

years = int(current_year) - int(birth_year)
print(years)

if  years >= 18 :
    print("you are allowed to enter")
else:
    print("you are a minor, cannot enter")