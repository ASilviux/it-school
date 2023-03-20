def is_even(number):
    # scop local
    if number % 2 == 0:
        return number

    
def add_one(number):
    # scop local
    number += 1
    
# Main
# scop global
a = 3

start_in = int(input("Start: "))
stop_in = int(input("Stop: "))

print(f"Produsul sumelor din intervalul {start_in} si {stop_in} este {range_product(start_in, stop_in)}")
a_even = is_even(a)
# a_even = False

print(f"Variabila a este numar par? {a_even}")

print(f"a = {a}")
add_one(a)
print(f"a = {a}")
# End main