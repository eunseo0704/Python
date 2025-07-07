# 45-1 
a = int(input("행 수: "))
for i in range(1, a + 1):
    for j in range(i):
        print("*", end=' ')
    print()

# 코테연습
a = int(input("행수: "))
for i in range(1,a+1):
    for j in range(i):
        print("*", end=" ")


# # 45-2
a = int(input("행 수: "))
for i in range(a, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# # 코테연습
a = int(input("행 수: "))
for i in range(a,0,-1):
    for j in range(i):
        print("*", end=" ")


# # 45-3
a = int(input("행 수: "))
for i in range(1, a+1):
    for j in range(a-i):
        print(' ', end = ' ')
    for j in range(i):
        print('*', end = ' ')
    print()

# # 코테연습
a = int(input("행 열: "))
for i in range(1, a+1):
    for j in range(a-i):
        print(' ', end=' ')
    for j in range(i):
        print("*", end='')
    print()

# # 45-4
a = int(input("행 수: "))
for i in range(a, 0, -1):
    for j in range(a-i):
        print(' ', end = ' ')
    for j in range(i):
        print('*', end = ' ')
    print()

# # 코테연습
a = int(input('행 열: '))
for i in range(a,0,-1):
    for j in range(a-i):
        print(' ', end='')
    for j in range(i):
        print(' ',end=' ')

# 피라미드
a = int(input("행 열: "))
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))