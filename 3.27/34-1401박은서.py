fruit = []
a = input()
while True:
    if len(fruit) == 5:
        break

    if a in fruit:
        print("이미 있다")

    else:
        fruit.append(a)
    f = input()
print(fruit)