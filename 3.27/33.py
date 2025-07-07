while True:
    n = int(input())
    if n % 5 == 0 and n != 0:
        print('5의 배수')
    elif n % 5 > 0:
        print('5의 배수 아님')
    if n == 0:
        print("반복 종료")
print("end")