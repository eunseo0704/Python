import random as r
num = list(range(1, 11))

while True:
    a, b = r.choices(num, k=2)
    if a==b:
        print(f'{a} ~ {b} => {a}')
        break
    else:
        if a<b:
            sum = 0
            for i in range(a, b+1):
                sum += i
            print(f'{a} ~ {b} => {sum}')
        else:
            for i in range(b, a+1):
                sum += i
            print(f'{b} ~ {a} => {sum}')