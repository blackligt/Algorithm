'''
스위치 켜고 끄기 문제
남자는 자신이 받은 숫자의 배수되는 스위치의 상태를 변경, 여자는 받은 숫자의 좌우 상태를 확인 대칭을 어디까지 이루는 지 확인하고
대칭을 이루는 범위 만큼의 스위치 상태를 변경
'''

'''
첫 코드를 완성한 후 테스트에서 문제 발생
스위치 번호는 인덱싱 번호와 달리 1부터 시작하기에 index = num - 1 코드를 넣어주는 것으로 실제 스위치 변경 위치를 조정
'''

num_switch = int(input())
status = list(map(int, input().split())) 
num_student = int(input())

for i in range(num_student):
    sex, num = map(int, input().split())
    index = num-1

    if sex == 1:
        i = 0
        while(True): #배수인 부분에 대해서 상태를 변경
            if (index + num*i) > num_switch-1:
                break
            else:
                if status[index + num*i] == 1:
                    status[index + num*i] = 0
                else:
                    status[index + num*i] = 1
                i += 1
        
        #print(sex, num)
        #print(status)
    
    else:
        i = 0
        while(True):
            if index - i < 0 or index + i >  num_switch - 1:
                i -= 1
                break
            elif status[index-i] == status[index+i]: #대칭인 부분까지 검색
                i += 1
            else:
                i -= 1 # 대칭이 아닌 부분 포함하지 않기
                break
        
        #print("i = ",i)

        for j in range(index-i, index+i+1, 1): #대칭인 부분 상태 변경
            #print("index = ", j)
            if status[j] == 1:
                status[j] = 0
            else:
                status[j] = 1
        
        #print(sex, num)
        #print(status)

row = num_switch // 20
col = num_switch % 20

i = 0
while(i != row):
    for j in range(20):
        print(status[20*i+j], end = ' ')
    print()
    i += 1

for j in range(col):
    print(status[20*i + j], end= ' ')

print()