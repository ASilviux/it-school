

def range_odd_number(start , stop):
    for i in range(start , stop):
        if i % 2 !=0:
            print (i)
        else: i+=1

start_in = 1
stop_in = 50

print(f"Produsul sumelor din intervalul {start_in} si {stop_in} este {range_odd_number(start_in, stop_in)}")