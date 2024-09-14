'''
골드바흐의 추측 문제
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
백만 이햐의 모든 짝수에 대해서 이 추측을 검증하는 프로그램을 작성하시오.

0을 입력하면 프로그램 종료

이는 특정 숫자까지의 소수들의 리스트를 구한 다음 참고로 100만이하의 짝수에 대해서이니 백만까지의 소수를 미리 구해놓을 수 있을 듯 하다.
소수의 리스트를 구한 다음 특정 수 n 이하에 대해서 소수의 합으로 이루어져 있는지 확인한다.

일단 소수의 리스트를 구하는 것부터 시작하자. --> 소수 구하는 알고리즘
코드를 어럼풋이 기억하고 있지만, 일단 나만으 방식으로 코드를 짜 보자
'''

'''
2단 반복문 i,j를 둘다 3부터 시작하는 것이 시간이 오래걸린다고 생각했다
따라서 i는 작은 3부터 시작하고 j는 큰 곳 부터 시작하면 어떨까?
'''

def finding_prime(max_num): #백만까지의 소수를 구하는 함수
    is_prime = [True]*(max_num+1)
    p = 2
    while (p*p < max_num+1):
        if is_prime[p]:
            for i in range(p*p, max_num+1, p):
                is_prime[i] = False
        p += 1
    return is_prime #소수인지 아닌지를 나타내는 리스트를 반환

max_num = 1000000
prime = finding_prime(max_num) #소수를 찾는데 오랜 시간이 걸리지 않는다.

while(True):
    n  = int(input()) #들어오는 모든 n은 짝수이다.
    if n == 0:
        break
    
    if n%2 == 1:
        print("Goldbach's conjecture is wrong.")

    else:
        is_find = False
        
        for i in range(3, n//2+1, 2): #3부터 진행되는 홀수들의 모음
            j = n-i #i+j = n을 유지
            if prime[i] and prime[j]:
                print(f"{n} = {i} + {j}")
                is_find = True
                break
        
        if is_find == False:
            print("Goldbach's conjecture is wrong.")

'''
gpt로 시간초과를 해결해 보려고 했으나 실패, 블로그를 통한 정답 확인
다음에 다시 풀어보기

정답코드를 분석한 결과 알고리즘의 차이는 존재하지 않았고 수를 어떻게 입력받는가로 정해지는 경우였다.

그렇다면 이 경우 import sys

n = int(sys.stdin.readline())

--> 다음은 정답코드
import sys

# 소수를 미리 계산하는 함수 (에라토스테네스의 체)
def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

# 1,000,000까지의 소수를 미리 계산
max_num = 1000000
is_prime = sieve_of_eratosthenes(max_num)

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

# 각 짝수에 대해 처리
for line in data:
    n = int(line)
    if n == 0:
        break
    
    found = False
    for i in range(3, n//2 + 1, 2):  # i는 3부터 n//2까지 홀수만 탐색
        if is_prime[i] and is_prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            found = True
            break
    
    if not found:
        print("Goldbach's conjecture is wrong.")
'''