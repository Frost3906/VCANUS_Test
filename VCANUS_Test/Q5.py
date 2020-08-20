
import copy

with open('VCANUS_Test\\resource\\pond.txt', mode='r', encoding='utf-8') as f:
    pond = []
    for line in f.readlines():
        pond.append(line.rstrip().split(" "))
    
for i in range(len(pond)):
    for j in range(len(pond[i])):
        pond[i][j] = int(pond[i][j])




depth = 0
while True:
    tmp = copy.deepcopy(pond)
    for i in range(1,len(pond)-1):
        for j in range(1,len(pond[i])-1):
            if pond[i][j] > 0:
                if (pond[i][j] <= pond[i-1][j]) and (pond[i][j] <= pond[i][j-1]) and (pond[i][j] <= pond[i][j+1]) and (pond[i][j] <= pond[i+1][j]):
                    pond[i][j] = pond[i][j] +1
                    
    if tmp == pond:
        for i in range(len(pond)):
            for j in range(len(pond[i])):
                depth += pond[i][j]
        break


for i in range(len(pond)):
    for j in range(len(pond[i])):
       print(pond[i][j],end=" ")
    print()

print("\n연못의 깊이의 총 합은 "+str(depth))
