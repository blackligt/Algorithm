'''
날짜 계산 문제
우리가 알고있는 연도가 새롭게 계산될 때 각 범위에 따른 나머지로 연도를 나타낸다고 할 수 있다.
E 는 15로 나눈 나머지, S 는 28로 나눈 나머지, M은 19로 나눈 나머지로 할 수 있다. 이때 나머지가 0인 경우는
나누는 수의 배수라고 볼 수 있다.

이 문제가 브루트 포스 문제인 이유는 나누는 수와 나머지가 주어지는 상황에서 나눠지는 수, 연도를 구해야 하기 떄문에
전체 탐색 문제라고 할 수 있다.

이를 더욱 빠르게 풀기 위해서는 전체를 확인할 필요가 없고 어떤 수의 배수에 더하기 나머지를 한 수 위주로 확인하면 될 것 같은데..
가장 큰 수인 28의 배수 + E한 숫자를 바탕으로 비교하면 될 듯 하다.

첫 번째 제출에서 시간초과 발생함
'''

diff_year = list(map(int,input().split()))

check_year = diff_year[1]

while(True):
    e_year = check_year % 15
    m_year = check_year % 19

    if e_year == 0: e_year += 15
    if m_year == 0: m_year += 19

    if e_year == diff_year[0] and m_year == diff_year[2]:
        break
    else:
        check_year += 28

print(check_year)