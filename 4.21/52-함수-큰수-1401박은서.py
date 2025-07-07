# 크기 비교 함수 정의
def maxp(x, y):
    if x >= y :
        return(x)
    else:
        return(y)

#인자 전달
print(f'큰 수: {maxp(10, 20)}')

#인자를 표준 입력 받아 전달
a, b = map(int,input("숫자: ").split())
print(f'큰 수: {map(a, b)}')