'''
사탕게임 문제
n*n 의 격자가 주어지고 서로 다른 사탕이 랜덤하게 격자 안에 주어진다.
사탕의 색이 다른 인접한 두 칸을 정하고 두 칸의 사탕을 서로 교환한다. 다음으로 같은 색으로 이루어져 있는 가장 긴 연속되는 부분을 제거한다
상태가 주어졌을 때 제거할 수 있는(먹을 수 있는) 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력 n이 주어지고 n개의 줄에 n개의 사탕 색상이 주어진다. 

여러 번 칸의 사탕을 교환하는 것이 아니라, 한 번 교환한 다음, 같은 줄에 있도록 한 사탕중에 최대가 되는 경우가 얼마인지를 구해내는 것
--> brute force 문제답게, 색이 다른 두 칸을 전부 교환해 본 다음, 최대가 되는 경우를 골라야 할 것 같다.


시간초과가 뜨는 상황에서 힌트를 받음
한 쌍을 변경한 후 연속되는 최대 갯수를 체크하는데 이 경우 전체 격자에서 확인할 필요가 없었다.
다른 곳에서의 변화는 없기에 변화가 생긴 행과 열에 대해서만 확인을 진행하면 된다.
그런데 이 경우 다른 곳에서 이미 최대가 있다면? --> 그렇다면 먼저 기존 것을 가지고 카운트를 한 다음에 변경을 진행하자
'''

import sys
import copy

n = int(sys.stdin.readline())
arr = []*n

'''
input = sys.stdin.read
data = input().splitlines()

for l in data:
    l_list = list(l)
    arr.append(l_list)

'''

for i in range(n):
    line = input()
    line_list = list(line)
    arr.append(line_list)

#print(arr)
check = [(0,1),(0,-1),(-1,0),(1,0)] #우측, 좌측, 위, 아래
ans = 0

# 위치를 바꾼 다음, 비교하는 것을 하나의 과정으로 반복하기, 그렇다면 각 칸에 대해서 4번의 자리 이동과 그 때의 격자를 다시 전부 검사해야하나
for i in range(n*n): 
    x, y = i//n, i%n #현재 확인하고자하는 위치
    #print("x and y : ",x, y)
    near = list([x - pos[0], y - pos[1]] for pos in check) #주변 격자들의 위치 튜플 리스트
    #print("near x and near y",near)
    for near_x, near_y in near: #상하좌우로 위치 변경
        if near_x >= 0 and near_x < n and near_y >= 0 and near_y < n: #격자 안에 있다면
            #print(near_x, near_y)
            new_arr = copy.deepcopy(arr) #새로운 격자 생성
            temp = new_arr[x][y]
            new_arr[x][y] = new_arr[near_x][near_y]
            new_arr[near_x][near_y] = temp
            #print(new_arr)
            for j in range(n*n):
                hor_len = 1
                hie_len = 1
                row, col = j//n ,j%n
                check_c = new_arr[row][col] #비교하고자하는 문자
                while(row < n-1):
                    row += 1
                    if new_arr[row][col] == check_c: #아래쪽 변수가 같다면
                        hor_len += 1 #숫자 한 개 증가
                    else:
                        break
                if hor_len > ans:
                    #print("new : !!!!",hor_len)
                    ans = hor_len
                row, col = j//n, j%n #위치 리셋
                while(col < n-1):
                    col += 1
                    if new_arr[row][col] == check_c: #옆쪽 변수가 같다면
                        hie_len += 1 #숫자 한 개 증가
                    else:
                        break
                if hie_len > ans:
                    #print("new : !!!",hie_len)
                    ans = hie_len

print(ans)