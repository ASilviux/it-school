def cutie(inaltime , latime, lungime, tip):
    pret =inaltime * latime * lungime * 25
    if tip == 2:
        return (pret * 0.1)+pret
    if tip == 3:
       return (pret * 0.2)+ pret
    
    

h= input("Inaltimea: ")
l= input("Latime: ")
lun= input("Lungime: ")
tip= input("Tip carton: ")
print(f"Pretul este {cutie(h, l, lun, tip )}")