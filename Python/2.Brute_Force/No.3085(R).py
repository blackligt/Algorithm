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

'''
def check(board, n):
    max_count = 1  # 연속된 사탕의 최대 개수

    # 각 행에 대해 연속된 사탕 개수 계산
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    # 각 열에 대해 연속된 사탕 개수 계산
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count

def solution():
    n = int(input())  # 보드 크기
    board = [list(input()) for _ in range(n)]  # 사탕 배열

    result = 0

    # 인접한 칸끼리 교환
    for i in range(n):
        for j in range(n):
            # 오른쪽 사탕과 교환
            if j + 1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 교환
                result = max(result, check(board, n))  # 교환 후 최대 개수 계산
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 원상복구

            # 아래쪽 사탕과 교환
            if i + 1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 교환
                result = max(result, check(board, n))  # 교환 후 최대 개수 계산
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원상복구

    print(result)

# 메인 함수 호출
solution()
'''

'''
도저히 모르겠음. 힌트를 받아야 할 것 같다.
방법은 교환한 후 최대 갯수를 계산, 그 뒤 다시 원상복귀 시키면 된다.
오른쪽으로만 교환하고 아래로만 교환하는 방식은 맞았음
해설에서는 전체 배열에 대해서 전부 연속을 확인했지만, 오르쪽 교환시 행 1개, 열 2개 아래로 교환시 행 2개 열 1개를 확인하는 식으로
하면 더 빠를 수 있을 듯 하다.
너무 어렵게 생각했다. 또한 코드를 정갈하게 작성하는 방법을 배워야 할 듯 하다.
'''
