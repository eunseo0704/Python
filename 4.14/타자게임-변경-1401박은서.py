# import random
# import time

# w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
# input('[타자게임] 준비되면 엔터')
# cnt = 0
# start = time.time()
# random.shuffle(w)
# while cnt < 5:
#         print(f"[문제 {cnt+1}]")
#         q = random.choice(w)
#         print(q)
#         ans = input()
#         if ans == q:
#             cnt += 1
#             print("pass")
#         else:
#             print("fail")
# end = time.time()
# re = end - start
# print(f'타자시간: {re:.2f}초')


import random
import time

animals = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']

def typing_game():
    input('[타자게임] 준비되면 엔터')
    
    start_time = time.time()
    
    correct_count = 0

    while time.time() - start_time < 10:
        animal = random.choice(animals)

        print(f"타이핑하세요: {animal}")

        user_input = input("입력: ")

        if user_input == animal:
            correct_count += 1
        else:
            print("fail")

    print(f"게임 종료! 10초 동안 {correct_count}개를 맞췄습니다.")

typing_game()
