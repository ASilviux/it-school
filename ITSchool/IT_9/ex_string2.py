lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#print(lorem.count(" ") +1)

words = lorem.split(" ")
#for word in words:
#    print(word)

#histogram = {}
#for k , v in histogram.items():
#    print(k, " - ", v )

#word2 =[]
#for word in words:
#    word2.append(word.lower())

for i , v in enumerate(words):
    words[i] = v.strip(",.?!:/ ")
