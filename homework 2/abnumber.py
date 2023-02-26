a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a>b:
    print("The sum of a+b is " + str(a+b))
    print("The difference of a-b is " + str(a-b))
elif a==b:
    print( "a at the power of b is " + str(a**b))
else:
    print("The sum of the number is: " + str(a+b))
