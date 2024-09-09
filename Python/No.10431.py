'''
이 문제는 정렬하는 알고리즘을 구현하는 문제이다. --> 어떤 정렬인지는 나중에 검색하기
이때 몇 번의 이동이 발생하는지 구하는 문제
자기 앞에 자기보다 큰 학생이 없다면, 자신이 맨 뒤에 서는 것이 맞음 --> 이동 없음
자기 앞에 자기보다 큰 학생이 1명이라도 있다면, 이 경우 그 전에 사람들은 다 오름차순으로 정렬되어 있음
--> 자기보다 큰 사람 중 가장 앞에 있는 사람의 바로 앞에 선다 --> 그럼 오름차순으로 정리가 된다.
실제로 정렬을 하면서 갯수를 카운트 하는 문제 --> 실제로 정렬을 해야하나? 시간이 오래걸림
그냥 자기보다 큰 개 몇 개 있는지만 확인하면 되는 문제
'''

p = int(input())

for i in range(p):
    answer = 0
    height_list = list(map(int,input().split())) #이 부분에서 틀렸는데, map, int를 통해서 전부 int로 바꾸어 주니까 해결됨, 알고리즘 문제는 아니었던 걸로
    for j in range(1,21,1):
        count = 0
        for k in range(1,j,1):
            if height_list[k] > height_list[j]:
                count += 1
        answer += count
    
    print(f"{height_list[0]} {answer}")