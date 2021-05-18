import os

lists = os.listdir("data/lyrics")

total =0
j=0
for j,i in enumerate(lists):
    words_file = open("data/lyrics/"+i,"r")
    total+=len(words_file.read().split(" "))
    words_file.close()

print(total/50)
