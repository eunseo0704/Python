fee = 850  #정해진 요금
card = int(input("카트 잔액: "))  #교통카드에 있는 금액 입력
if card>=fee:
    print("탑승 가능")
else:
    print("탑승 불가능")