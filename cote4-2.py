"""
첫째 줄에 정수 입력
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력
"""

n = int(input())
ct = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                ct += 1

print(ct)