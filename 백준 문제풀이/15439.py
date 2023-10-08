# 15439 번 문제 

# 순열 문제 
'''
상의 N벌, 하의 N벌이 있다. 
주어진 N에 대해서 상의 하의 가 서로 다른 색상인 조합의 가짓수를 구하는 문제.
(단, N개의 색상은 모두 서로 다르다.)
'''

from itertools import permutations
N = int(input())
N = [x for x in range(N)]
N = list(permutations(N,2))
print(len(N))

# itertools 라이브러리를 사용하지 않고 아래와 같은 순열방식으로도 풀 수 있다.  
print(N*(N-1))