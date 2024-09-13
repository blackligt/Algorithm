'''
최대공약수와 최소공배수 문제
두개의 자연수를 입력 받아 최대공약수와 최소 공배수를 출력하는 프로그램을 작성

각 자연수가 어떤 소수로 이루어져 있는지를 확인한다.
최대공약수는 두개가 겹치는 것만, 최소 공배수는 두 개 중 큰 제곱의 소수만 따로 빼서 
'''

a,b = map(int, input().split())
a_dic = dict()
b_dic = dict()
a_unique = set()
b_unique = set()

if a > b :
    big = a
else:
    big = b

for i in range(2,big+1):
    while(True):
        if a % i == 0: #i로 나누어 떨어진다면
            a = a/i
            if i not in a_dic:
                a_dic[i] = 1
                a_unique.add(i)
            else:
                a_dic[i] += 1
        else:
            break
    while(True):
        if b % i == 0: #i로 나누어 떨어진다면
            b = b/i
            if i not in b_dic:
                b_dic[i] = 1
                b_unique.add(i)
            else:
                b_dic[i] += 1
        else:
            break
    
    if a == 1 and b == 1: #약수를 다 찾은 경우
        break

# print("a_dic : ", a_dic)
# print("b_dic : ", b_dic)
# print("a_unique : ", a_unique)
# print("b_unique : ", b_unique)

inter = a_unique.intersection(b_unique) #교집합, 최대공약수
union = a_unique.union(b_unique) #합집합, 최소공배수
# print("inter : ", inter)
# print("union : ", union)

inter_answer = 1
union_answer = 1

for i in inter: #항상 a,b 동시에 값이 존재한다.
    if a_dic[i] > b_dic[i]:
        inter_answer *= i ** b_dic[i]
    else:
        inter_answer *= i ** a_dic[i]

for i in union:
    if i not in a_dic: #b에만 있는 경우
        union_answer *= i** b_dic[i]
    elif i not in b_dic: #a에만 있는 경우
        union_answer *= i** a_dic[i]
    elif a_dic[i] > b_dic[i]: #a,b에 있고 a가 더 큰 경우
        union_answer *= i** a_dic[i]
    else: #a,b 에 있고 b가 더 큰 경우
        union_answer *= i** b_dic[i]

print(inter_answer)
print(union_answer)

'''
어떤 방식으로 풀었는가
두 개의 수에 대해서 어떤 소수의 몇 제곱으로 이루어져 있는지를 직접 계산
최대공약수는 두 개의 수에 대해서 겹치는 소수에 대해서 겹치는 만큼의 제곱을 곱해야 한다.
최소공배수는 두 개의 수에 대해서 모든 소수를 최대의 제곱 만큼 해서 곱해야 한다.
'''