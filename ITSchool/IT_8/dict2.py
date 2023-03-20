dict1 = {
    "key1" : 1,
    "key2" : {
        "Key1" : 1,
        "key2" : ["elem1" , "elem2"]
    }
}

print(dict1)

dict1["key1"]=2
print(dict1["key1"])

dict1["key3"]=set()

print(dict1)
del dict1["key1"]
print(dict1)