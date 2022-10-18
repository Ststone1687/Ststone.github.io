import random
import math
import codecs

with open('input.txt') as f:
    lines = f.readlines()

inf = codecs.open("output.txt", "w", "utf-8")

for i in lines:
    add = ""
    for j in range(len(i)):
        if(i[j]=="<"):
            add += "&lt;"
        elif(i[j]==">"):
            add += "&gt;"
        else:
            add += i[j]
    inf.write(add)

print("finish")