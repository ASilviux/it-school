import_numbers = "today we have 200 clients"
user_name= "mihai.dinu"

#prima litera mare
print(import_numbers.capitalize())

#lower and upper toate literele mici sau mari
print(import_numbers.lower())
print(import_numbers.upper())

#prima litera din fiecare cuvand 
print(import_numbers.title())

#replace caracter string numbers, sau sa eliminam/inlocuim 
new_numbers = import_numbers.replace("clients" , "customers")
print(new_numbers)