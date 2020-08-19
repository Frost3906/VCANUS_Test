# 재귀함수의 stack overflow 를 해결하기 위해서는 tail recursion 을 이용해 스택 호출을 줄이는 방법이 있으나
# python 은 tail recursion 을 지원하지 않습니다.

# def factorial_v2(x, acc=1):
#     if(x==0):
#         return acc
#     return factorial_v2(x-1,x*acc)

# result = factorial_v2(999)
# print(result)


# 따라서 단순 반복문을 통해 factorial 함수를 구현해 보았습니다.

def factorial_v2(x):
    result=1
    while True:
        if x == 1:
            return result
        result *= x
        x-=1
 
result = factorial_v2(999)
print(result)