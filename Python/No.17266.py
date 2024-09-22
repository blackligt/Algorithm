'''
어두운 굴다리 문제
가로등과 거리가 주어졌을 때 최소한의 자원으로 모든 거리의 길을 밝히는 문제
특정 위치에서 길이가 최소 어느정도 되어야 모든 길을 밝힐 수 있는 지를 찾아내야 한다.
입력을 굴다리의 길이 n 가로등의 개수 m, m개의 가로등이 설치될 위치인 x가 주어진다. x는 오름차순으로 입력된다.
단순하게 생각하면, 가로등 사이의 길이가 가장 긴 부분을 찾은 후 이것을 2로 나누어 최소한 필요한 길이를 찾아내면 될 것이라 판단된다

처음과 마지막 부분은 조명이 더 존재하기 않기 떄문에 나중에 2로 나누는 길이를 고려해 2배를 할 필요가 있다.
'''

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x.insert(0,0)
x.append(n)

longest_dis = 0
for i in range(len(x)-1):
    dis = x[i+1]-x[i]
    if i == 0 or i == len(x)-2:
        dis = dis*2
    if dis > longest_dis:
        longest_dis = dis

max_height = 0

if longest_dis % 2 == 0:
    max_height = longest_dis/2
else:
    max_height = longest_dis/2 + 1

print(int(max_height))