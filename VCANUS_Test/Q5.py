with open('VCANUS_Test\\resource\\pond.txt', mode='r', encoding='utf-8') as f:
    pond = []
    for line in f.readlines():
        pond.append(line.rstrip().split(" "))
    

print(pond[0])
print(pond[1])
print(pond[2])
print(pond[3])
print(pond[4])
print(pond[5])
print(pond[6])
print(pond[7])
print(pond[8])
print(pond[9])

for i in pond:
    for