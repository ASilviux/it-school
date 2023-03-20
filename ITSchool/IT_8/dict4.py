students_grades ={
    "Ana" : 9.5,
    "Ioan" : 8.0,
    "MAria" : 7.5,
    "Andrei" : 9.0,
    "Elena" : 10.0 
}

nota = students_grades.get("Ana")

#       is not 
if nota != None:
    print(nota)
else:
    print("Studentul nu exista")

lista_chei = students_grades.keys()
print(type(lista_chei))
print(lista_chei)

#cum extragem lista de chei
for name in lista_chei:
    print(name)

for key in students_grades.keys():
    print(key)

print("-" *30)

#cum extragem lista de  valori
for values in students_grades.values():
    print(values)

print("-"*30)

#cum extragem perechi cheie/valori
valori= students_grades.items()
print(list(valori)[0])

#double unpacking
for v in valori:
    name, grade = v
    print(name, grade)