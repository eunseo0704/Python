#51-1
# 합계 함수 정의
def fun_s(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

#main
# 합계 함수 호출
print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))


#51-2
def fun_fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

#main
print(fun_fact(5))
print(fun_fact(10))