students_grades ={
    "Ana" : 9.5,
    "Ioan" : 8.0,
    "MAria" : 7.5,
    "Andrei" : 9.0,
    "Elena" : 10.0 
}

print(students_grades["Ana"])
print(students_grades.get("Ana"))

nota = students_grades.get("Ana")

#       is not 
if nota != None:
    print(nota)
else:
    print("Studentul nu exista")