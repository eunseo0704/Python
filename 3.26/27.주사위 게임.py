user = list(map(int, input('2개 입력(1~6, 중복 허용): ').split()))
dice = [r.randint(1, 6), r.randint(1, 6)]

print(f"Com: {dice}")
print(f'User: {user}')

if sorted(dice) == sorted(user):
    print("1등")
elif user[0] in dice or user[1] in dice:
    print("2등")
else:
    print("3등")