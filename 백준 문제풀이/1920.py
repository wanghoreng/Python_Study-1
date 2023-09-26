# 1920번 문제

# 문제 내용 
'''
N 개의 정수로된 배열이 주어지는데, 
이 배열안에 입력받은 값이 존재하는지 찾는 문제 
'''

# 문제 해결방식 
'''
원래 count() 함수를 사용하기 위해서 입력받는 배열들을 str 함수로 
형변환을 했었는데, 시간초과가 났었다. 
그 이유를 알고보니 list 의 search 는 처음부터 값이 나올때까지 
순차탐색을 하는 방식이기 때문에 
시간복잡도 O(n) 이 된다. 
set 의 search sms O(1) 로, 탐색 필요없이 바로 search 가 
완료되는 것으로 시간 초과가 뜨지 않았다.
'''

import sys 
N = sys.stdin.readline()
A = set(sys.stdin.readline().split())
M = sys.stdin.readline()
B = sys.stdin.readline().split()

# count() 함수는 문자열만을 인자로 받으며, set Object 에는 없는 이용할 수 없는 함수이다. 
for i in B : 
  if i in A :  # LIST 내에 i 가 존재한다면, True, 아니면 False 를 반환한다.
    print(1)
  else : 
    print(0)

'''
다른 사람풀이를 보니, 이진 탐색으로 푼 것같았다. 
나는 아직 이진탐색을 공부하지 않았는데 이제 슬슬 알고리즘을 배워야겠다는
생각이 들었다. 
'''