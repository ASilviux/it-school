#set-ul elimina duplicatul
#nu printeaza in ordine ce random

colors = {"red" , "brown" , "blue" , "white"}

print(colors)
print(type(colors))

#dictionar nu e un set gol
colors1={}
print(type(colors1))


for i in colors:
    print(i)

colors.add("black")

color_list=list(colors)
color_list.sort
print(color_list)

colors.remove("white")
print(colors)


