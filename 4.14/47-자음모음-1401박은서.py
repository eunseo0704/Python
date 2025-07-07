sen = input("영문자열 입력: ")

vow = 'aeiou'
# con = 'bcdfghjklmnpqrstvwxyz'
vow_c, con_c = 0, 0
sen.lower()

for i in sen:
    if i.isalpha():
        if i in vow:
            vow_c += 1
        else:
            con_c += 1
print(f'#'*20)
print(f'자음: {con_c}개, 모음: {vow_c}개')  