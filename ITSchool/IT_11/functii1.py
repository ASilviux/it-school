

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
a = 3

a_even = is_even(a)

print(f"Variabila este numar par? {a_even}")