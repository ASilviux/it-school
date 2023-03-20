name_grade={
    "Alex" : [6,7,8],
    "Maria" : [5,8,9],
    "Andrei" : [4,7,5]
}

for n , g in name_grade.items():
    media= sum(g) / len(g)
    print(n + " are media " + str(media))
    print(n,media)