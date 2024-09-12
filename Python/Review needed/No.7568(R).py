'''
8979문제 올림픽과 비슷한 문제이나, 전체의 등수를 구하고 이를 출력하는 문제
일단 키로 정렬을 하고 처음부터 몸무게를 비교하여, 몸무게가 다음 차례보다 많으면 등수 메기고 +1,
몸무게가 다음 차례보다 적으면 등수 메기고 등수 그대로 유지하기, 이렇게 할 경우 각 사람별 등수를 정할 수 있을 것이라고 생각된다.
효율적인지 알 수 없지만, 몸무게로 sort한 후 위의 단계를 진행, 다시 입력 순서로 sort를 한 후 등 수를 출력?
'''

'''
3번의 시도 후 계속 오답이 나온다. 처음의 알고리즘에 무슨 문제가 있다고 판단된다.
1번째 시도, 리스트를 정렬할 때 키와 몸무게 2가지 전부를 바탕으로 정렬 --> 실패
2번째 시도, 키로 정렬 후 몸무게를 비교할 때, 키가 동일한 경우 
'''

#다음에 다시 도전하자 (첫번째 도전 2024.09.10 오후 1시)

n = int(input())
how_big = []
rank = 1
same_rank = 0

for i in range(n):
    height, weight = map(int,input().split())
    how_big.append([i,height,weight])

how_big.sort(key=lambda x: (x[1], x[2]), reverse=True) #리스트를 키가 큰 순서로 정렬

for i in range(len(how_big)): # 등수 매기기
    if i == len(how_big)-1:
        how_big[i].append(rank)
    elif how_big[i][2] > how_big[i+1][2]:
        how_big[i].append(rank)
        rank += same_rank + 1
    elif how_big[i][2] <= how_big[i+1][2]:
        how_big[i].append(rank)
        same_rank += 1
    
# for i in range(len(how_big)):
#     print(how_big[i])

how_big.sort(key= lambda x:x[0])

for i in range(len(how_big)):
    if i == len(how_big)-1:
        print(how_big[i][3])
    else:
        print(how_big[i][3], end= ' ')