# 한 줄씩 읽기
# readlines()
f = open("data_2.txt","r")

lines = f.readline()
print(lines)

for line in lines:
    print(line)  # print(line.strip())
f.close()