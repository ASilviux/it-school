dict1 = {
    "key1" : 1,
    "key2" : {
        "Key1" : 1,
        "key2" : ["elem1" , "elem2"]
    }
}
print(dict1)

lista_dict= dict1["key2"]
print(lista_dict)

print(dict1["key2"]["key2"])