import random as r
import time

w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
input('[타자게임] 준비되면 엔터')
cnt = 0
start = time.time()
while cnt < 5:
        print(f"[문제 {cnt+1}]")
        q = r.choice(w)
        print(q)
        ans = input()
        if ans == q:
            cnt += 1
            print("pass")
        else:
            print("fail")
end = time.time()
re = end - start
print(f'타자시간: {re}초')