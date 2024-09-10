'''
쿠키의 신체 측정, n*n 배열 형태로 입력을 받은 후 심장 부분을 찾아내고, 그 다음 위치에 따라서 몇개의 칸들로 이루어져있는지를 확인하는 문제

쿠키의 머리와 심장이 어디에 있는지 확인을 한 후 심장을 중심으로 왼쪽 팔, 오른쪽 팔, 허리를 측정
허리의 끝 부분에서 다리 시작점을 알아내고, 왼쪽 다리 오른쪽 다라가 각각 몇칸 내려가 있는지를 측정
이를 공백으로 구분하여 출력하기
'''

n = int(input())
matrix = []
heart = [0,0]
is_head = True
size = [0]*5

for i in range(n): #행렬 채우기
    inner_matrix = []
    line = input()
    for c in line:
        if c == '_':
            inner_matrix.append(0)
        else:
            inner_matrix.append(1)
            if is_head: #처음 등장하는 * 부분이 머리인 것을 확인
                heart = [i+1,line.index(c)]
                is_head=False
    matrix.append(inner_matrix)

for i in range(1,n): #왼쪽 팔
    if heart[1]-i < 0:
        break
    elif matrix[heart[0]][heart[1]-i] == 1:
        size[0] += 1
    else:
        break

for i in range(1,n): #오른쪽 팔
    if heart[1]+i > n-1:
        break
    elif matrix[heart[0]][heart[1]+i] == 1:
        size[1] += 1
    else:
        break

for i in range(1,n): #허리
    if matrix[heart[0]+i][heart[1]] == 1:
        size[2] += 1
    else:
        end_waist = [heart[0]+i-1, heart[1]]
        break

for i in range(n): #왼쪽 다리
    if end_waist[0]+1+i > n-1:
        break
    elif matrix[end_waist[0]+1+i][heart[1]-1] == 1:
        size[3] += 1
    else:
        break

for i in range(n): #오른쪽 다리
    if end_waist[0]+1+i > n-1:
        break
    elif matrix[end_waist[0]+1+i][heart[1]+1] == 1:
        size[4] += 1
    else:
        break

print(heart[0]+1, heart[1]+1) #첫번째 칸이 (1,1)

for i in size:
    print(i, end=' ')
print()