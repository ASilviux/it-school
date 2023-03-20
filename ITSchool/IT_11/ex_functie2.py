

def volum(h , r):
    v = float((3.14 * h * r^2 )/1000)
    return v
    

h= input("Inaltimea: ")
r= input("Raza: ")

print(f"Volumul cilindrului este este {volum(h, r)}")