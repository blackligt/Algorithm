'''
비밀번호 발음하기 문제, 문자열이 조건에 맞는지를 확인하는 문제
모음이 반드시 하나 포함, 모음 연속 3개, 자음 연속 3개 블가, 같은 글자 연속 불가, 단 ee,oo 는 허용
end 가 입력되면 프로그램 종료
'''

finish = False
vowels = ['a','e','i','o','u']
prev = ['e','o']


while(not finish):
    check = [0,1,1]
    seq_check = 0
    prev_c = ''
    password = input()
    
    if password ==  'end':
        finish = True
        continue

    for c in password:
        if c in vowels: #모음이면
            check[0] = 1
            if seq_check <= 0: #앞쪽이 모음이었다면
                seq_check -= 1
            else :
                seq_check = -1

        else: # 자음이면
            if seq_check >= 0: #앞쪽이 자음이었다면
                seq_check += 1
            else:
                seq_check = +1

        if prev_c not in prev and prev_c == c: #e,o 가 아니고 연속인 경우
            #print("double error")
            check[2] = 0
            break

        if seq_check == -3 or seq_check == 3: #모음이나 자음이 3개 연속이면
            check[1] = 0
            #print('seqential error')
            break
            
        prev_c = c
        
    if check == [1,1,1]:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")        