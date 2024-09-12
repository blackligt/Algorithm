'''
크로스 컨트리 문제
각 팀별로 등 수 별 점수를 더해서 가장 잘한 팀을 고르는 것, 각 팀은 6명, 6명이 되지 않는 팀은 점수가 계산되지 않는다.
4명의 점수로 팀 등수를 계산하고, 동점이면 5번째 주자가 빨리 들어온 팀이 우승이다.
입력으로는 테스트 케이스 개수, 각 테스트 케이스별 주자들의 수와 도착 순서별 주자의 팀 숫자가 입력된다.

구현을 할 때 팀 넘버는 set으로 구현을 하고, 새로운 팀 넘버가 들어오면, set에 추가하고 팀 별 리스트를 추가함
'''

'''
문제를 해결하다가 근본적인 문제를 발견함. --> 6명 선수가 안되는 팀은 점수가 아예 주어지지 않음
따라서 그 팀을 제외하고 점수를 매겨야 한다. 코드 다시 짜야 할 듯?
그렇다면 이 경우에 6명이되는 팀이 있는 지를 먼저 확인하고 그것만 남긴 다음에 점수를 측정해야 하나?
그런데 이 경우 전체 탐색을 2번이나 해야 하기에 시간 복잡도가 높이지지 않을까? 최대 1000개를 2번 체크하는 것이기에 딱히 문제는 없을 수도
'''

'''
결국 문제를 해결하지 못함. 런타임 에러가 발생함. gpt로 검색해 본 결과 딕셔너리를 이용해서 문제를 풀이하는 것을 확인 할 수 있었음
해설 코드는 각 팀 별로 선수들의 순서를 리스트화 하고 팀 넘버와 함꼐 딕셔너리화
딕셔너리 내 팀 선수 리스트가 6 이상인 것만 다시 딕셔너리화
딕셔너리 내 선수 리스트로 4번째까지 점수, 5번쨰 점수를 구하고 팀 번호와 함께, 이를 리스트화
리스트를 점수에 맞게 정렬한 후 가장 앞 쪽 팀 번호를 출력
'''

t = int(input())

for i in range(t): #각 테스트 케이스에 따라
    n = int(input())
    result = list(map(int, input().split()))
    team = set() #몇 개의 팀이 있는지 확인
    rank_team = set() #실제 6명을 만족하는 팀의 집합
    count = [] #몇 명의 선수가 있는 지 체크

    for s in result: #O(n) 6명을 만족하는 지 확인하는 반복문
        if s not in team:
            team.add(s)
            count.append(1) #team num - 1의 인덱스에 몇 번 등장했는지 넣음
        elif count[s-1] == 5: #팀이 6명이 만족한다면
            rank_team.add(s)
        else:
            count[s-1] += 1
        
    rank_team_list = list(rank_team) #리스트화 해서 인덱스를 실제 확인하기
    #print(rank_team_list)

    rank = [[0,0,0,0] for _ in range(len(rank_team_list))] #팀의 인덱스, 4번째 까지 점수, 5번째 점수, 몇 번 체크했는지
    score = 1

    for s in result: #팀 별로 점수 계산
        if s in rank_team:
            #print("to time :",s, "point : ", score)
            team_index = rank_team_list.index(s)
            if rank[team_index][3] == 0 :
                rank[team_index][0] = team_index
                rank[team_index][1] += score
                rank[team_index][3] += 1
            elif rank[team_index][3] <= 3 :
                rank[team_index][1] += score
                rank[team_index][3] += 1
            elif rank[team_index][3] == 4:
                rank[team_index][2] += score
                rank[team_index][3] += 1
            score += 1
        else:
            continue

    rank.sort(key=lambda x: (x[1], x[2]))
    print(rank)
    winner_index = rank[0][0] #이긴팀의 인덱스
    winner = rank_team_list[winner_index]

    print(winner)
        
    

        
    


