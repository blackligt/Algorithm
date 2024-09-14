'''
소수 찾기 문제
주어진 수 n 개 중에서 소수가 몇개인지 찾아서 출력하는 프로그램

소수는 1을 제외, 1과 자기 자신으로 밖에 나누어지지 않는 수를 의미한다.
1000이하의 자연수 100개 정도면 전체 탐색으로 진행해도 시간 소비가 크지 않을 것이라고 판단된다.
구한 소수를 set으로 저장해서, 나누는 수를 set안의 있는 수로 지정하면
시간을 더욱 단축 시킬 수 있을 것으로 판단된다.
'''

n = int(input())
l = list(map(int, input().split()))
answer = 0

for i in range(n):
    num = l[i] #우리는 num 이 소수인가 아닌가를 구해야 한다. 
    is_unique = True
    
    if num == 1:
        continue

    for j in range(2, num):
        if num % j == 0: # 소수가 아니라면
            is_unique = False
            break
    
    if is_unique == True:
        answer += 1

print(answer)