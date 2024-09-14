'''
일곱 난쟁이 문제
총 9명의 난쟁이가 있는데 진짜인 7명의 난쟁이 키의 합은 100이다. 9명의 키가 주어졌을 때 난쟁이들의 키의 합이 100이 되는 조합을
오름차순으로 정리해서 출력하세요. 입력에서 7개를 합하면 100이 되는 것은 무조건 있음

이는 9명 중에서 2명을 뺴는 것으로 생각할 수 있다.
'''
import sys

sum = 0
height = []
for i in range(9):
    n = int(sys.stdin.readline())
    sum += n
    height.append(n)

found = False
for i in range(8):
    if not found :
        for j in range(i+1,9):
            a = height[i]
            b = height[j]
            if sum - a - b == 100:
                #print(f"{sum} - {height[i]} - {height[j]} = {sum - height[i] - height[j]}")
                height.remove(a)
                height.remove(b)
                found = True
                break

height.sort()
for i in range(7):
    print(height[i])