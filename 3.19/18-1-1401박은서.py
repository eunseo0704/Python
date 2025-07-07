a = int(input("score: "))
# 효율이 떨어짐
if a >= 80:
    print("A")
if 60 <= a < 80:
    print("B")
if a < 60:
    print("C")
print("END")