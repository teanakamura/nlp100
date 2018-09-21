import os

print(os.getcwd())

f = open("./nlp100/hightemp.txt")
count = 0
for l in f:
    count += 1
print(count)
f.close()

f = open("./nlp100/hightemp.txt")
for i, l in enumerate(f, 1):
    pass
print(i)
f.close()

f = open("./nlp100/hightemp.txt")
print(sum(1 for line in f))
f.close()

#Unix command
#wc -l ./nlp100/hightemp.txt
