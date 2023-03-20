template = "Salut <<user>> ! <<user>>, nu te-am mai vazut de mult!"

user = input("Numele tau: ")

greet_msg = template.replace("<<user>>" , user)

print(greet_msg)