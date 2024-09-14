'''
약수 문제
어떤 수 a의 약수가 모두 주어졌을 때 a를 구하는 문제
이 경우 가장 작은 약수와 가장 큰 약수를 곱하면 a를 구할 수 있다.
약수가 한 개인 경우 그 약수를 곱하는 것으로 a를 구할 수 있다.
'''

num = int(input())
divisor = list(map(int, input().split()))
divisor.sort()

if num == 1:
    answer = divisor[0]**2

else:
    answer = divisor[0]*divisor[-1]

print(answer)