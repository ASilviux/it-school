print("Give me a number and i will tell you if it's even or odd  ")
number = input("Number: ")

rest = int(number)%2

if rest == 0:
    print("The number " +number+ " is even ")
else:
    print("The number " +number+ " is odd ")
