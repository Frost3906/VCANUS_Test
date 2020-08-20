문제 5
======================


## 1. pond.txt 파일을 pond 리스트로 받은 뒤 int 자료형으로 변환
	
<pre>
<code>
import copy 
with open('VCANUS_Test\\resource\\pond.txt', mode='r', encoding='utf-8') as f:
    pond = []
    for line in f.readlines():
        pond.append(line.rstrip().split(" "))
    
for i in range(len(pond)):
    for j in range(len(pond[i])):
        pond[i][j] = int(pond[i][j])
</code>
</pre>
 
 
## 2. 깊이를 출력할 depth를 준비하고 list를 순회하며 깊이를 조정하며 변화를 줌
### 2-1 tmp 리스트와 반복문을 활용해 깊이의 변화가 없을 때 까지 반복
<pre>
<code>
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
</code>
</pre>
                    
## 3. list를 순회하며 디지털 연못을 출력                   
<pre>
<code>
for i in range(len(pond)):
    for j in range(len(pond[i])):
       print(pond[i][j],end=" ")
    print()
</code>
</pre>
> 0 0 0 0 0 0 0 0 0 0 \
0 0 0 0 1 0 0 0 0 0 \
0 0 0 1 2 1 0 0 0 0 \
0 1 1 2 3 2 1 0 0 0 \
0 1 2 3 4 3 2 1 1 0 \
0 1 2 3 4 3 3 2 1 0 \
0 0 1 2 3 2 2 1 0 0 \
0 0 0 1 2 1 1 0 0 0 \
0 0 0 0 1 0 0 0 0 0 \
0 0 0 0 0 0 0 0 0 0      
      
## 4. depth에 담긴 연못의 깊이의 총합 출력
<pre>
<code>
print("\n연못의 깊이의 총 합은 "+str(depth))
</code>
</pre>

> 연못의 깊이의 총 합은 68
  

