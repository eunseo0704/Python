                                
                        
b,gender=input().split(',')

g=int(gender)

birthyear=int(b[:2])

if gender%2==0:
    s='여성'
else:
    s='남성'

if gender<3:
    a=2025-(birthyear+1900)+1
    print(f'현재나이 {a}살 {s}입니다.')
else:
    a=2025-(birthyear+2000)+1
    print(f'현재나이 {a}살 {s}입니다.')
                            