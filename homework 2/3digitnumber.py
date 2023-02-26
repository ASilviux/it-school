a =int(input("Enter a number: "))

if a<100 or a>999:
    print("Eroare")
elif((a%10)>= 5):
    print("the last number is: " + str(a%10))
    print("The sum of the numbers " + str(a + a%10))
else:
    print("the last number is: " + str(a%10))
    print("The difference of the numbers " + str(a - a%10))
