'''
각 국가별로 몇개의 메달이 있는지 미리 저장하고 비교하는 것이 필요하다. 그렇다면, 2차원 배열로 해야할 듯?
이때 주의해야할 점은, 메달이 모두 같으면 같은 등 수로 취급하고 다음 등 수는 건너뛴다는 것
전체 나라의 순위를 구할 필요가 없다. 구하려는 국가가 몇 등인지를 구하면 된다.
국가는 순서대로 입력되지 않는다.
'''

'''
c_count, c_num = map(int,input().split())
country = []
rank = 1

for i in range(c_count):
    medals = list(map(int, input().split())) #index 0~3, 0 c_num, 1~3 medals
    score = medals[1]*100 + medals[2]*10 + medals[3] #score of the country 
    # 이것 만으로는 무조건 금메달이 이긴다는 보장이 없다. 단순히 수를 크게하는 게 의미가 있을까? 다른 구분 방법을 찾아보아야 한다.
    country.append([medals[0], score])

for i in range(c_count):
    if country[i][0] == c_num:
        c_score = country[i][1]

for i in range(c_count):
    if country[i][1] > c_score:
        rank += 1

print(rank)
'''

c_count, c_num = map(int,input().split())
country = []
rank = 1

for i in range(c_count):
    medals = list(map(int, input().split())) #index 0~3, 0 c_num, 1~3 medals
    country.append(medals)

for i in range(c_count):
    if country[i][0] == c_num:
        gold = country[i][1]
        sliver = country[i][2]
        bronze = country[i][3]

for i in range(c_count):
    if country[i][1] > gold:
        rank += 1
    elif country[i][1] == gold and country[i][2] > sliver:
        rank += 1
    elif country[i][1] == gold and country[i][2] == sliver and country[i][3] > bronze:
        rank += 1

print(rank)