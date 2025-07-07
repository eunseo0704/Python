#추가
name = ['홍길동', '일지매']
print(f'현재 프로그래밍 수강 신청자는 {name} 입니다.')
a = input('추가할 학생 이름: ')
name.append(a)
print(f'{name} 학생의 신청이 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {name} 입니다.')

#삭제
b = input('철회할 학생 이름: ')
name.remove(b)
print(f'{b} 학생의 수강 철회가 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {name} 입니다.')

#변경
name = ['일지매', '전우치']
print(f'현재 프로그래밍 수강 신청자는 {name} 입니다.')
c = input('변경 전 이름: ')
d = input(f'변경 후 이름: ')
id = name.index(c)
name[id] = d
print(f'요청하신 대로 {c}을(를) {d}로 변경하였습니다.')
print(f'현재 이 과목의 최종 신청자는 {name}입니다.')