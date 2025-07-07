print("키(cm): ")
height = float(input())

print("체중(kg)")
weight = float(input())
print("#"*7)

if 130<=height<190 and 25<=weight<100:
    print("이용 가능")
else:
    print("이용 불가능")