'''
핵심은 입력된 사람들이 이름 중 중복된 것을 제외하고 몇명이 신청을 했는지를 확인하는 것과 
게임 인원을 바탕으로 몇 번으 게임을 진행할 수 있는지를 확인하는 문제
1. 리스트로 사람들 이름을 저장했더니, 시간초과가 발생했다. --> set으로 변경해서 구현해 볼 것
'''

#set을 통해서 시간초과 문제를 해결함, 간단하게 말하면 set은 해시함수를 이용하기에 list를 직접 비교하는 것 보다 시간복잡도가 작음
'''
if name not in list: list.append(name보다 set을 이용한 s.add(name)이 더 빠른 이유는 자료 구조의 차이에서 비롯됩니다. 각각의 동작 원리를 살펴보면 다음과 같습니다.

1. 리스트(list)의 동작 방식
리스트는 순차적으로 저장된 데이터 구조입니다. 리스트에서 특정 요소가 있는지 확인하려면, 리스트의 처음부터 끝까지 순차적으로 탐색해야 합니다. 따라서 리스트에서 name이 있는지 확인하는 if name not in list:는 최악의 경우 리스트의 모든 요소를 확인해야 하므로, 시간이 오래 걸릴 수 있습니다.

리스트에서 특정 요소를 찾는 데 걸리는 시간 복잡도는 **O(n)**입니다. (n은 리스트의 길이)
list.append(name)는 리스트의 끝에 요소를 추가하는 작업으로, 이 자체는 **O(1)**이지만, 중복 체크 과정이 느려집니다.
2. 셋(set)의 동작 방식
반면, set은 해시 테이블을 기반으로 동작하는 자료 구조입니다. set에서 요소를 추가하거나 중복 여부를 확인하는 연산은 해시값을 사용하여 요소를 관리합니다. 해시 테이블을 사용하면 특정 값이 존재하는지 확인하는 작업이 매우 빠릅니다.

set.add(name)에서 name이 이미 존재하는지 확인하는 작업은 해시 함수를 이용하기 때문에 **평균적으로 O(1)**의 시간 복잡도를 가집니다.
또한, set.add(name) 역시 **O(1)**로 동작합니다.
3. 차이점
정리하면, if name not in list:는 리스트의 길이에 비례하여 시간이 걸리는 O(n) 연산인 반면, set.add(name)는 평균적으로 O(1) 시간이 소요됩니다. 따라서 set을 사용하는 것이 리스트보다 훨씬 더 효율적입니다.

리스트: 요소가 많아질수록 중복 확인에 시간이 오래 걸림 (O(n)).
셋: 해시 테이블을 사용해 요소를 빠르게 찾고 추가 가능 (O(1)).
'''


count, game = input().split()
count = int(count)
names = set()

for i in range(count):
    name = input()
    names.add(name)

persons_num = len(names)
game_count = 0

if game == 'Y':
    game_count = persons_num
elif game == 'F':
    game_count = persons_num//2
elif game == 'O':
    game_count = persons_num//3

print(game_count)