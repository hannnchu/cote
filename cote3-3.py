"""
입력 조건)
첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다(1<=N,M<=100)
둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숙자는 1이상 10,000이하의 자연수이다.

출력 조건)
첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""

n,m = map(int,input().split())

output = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_data = min(data)
    output = max(output,min_data)

print(output)