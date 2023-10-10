# Greedy

# 숫자 카드 게임 (이코테 p96)
'''
1. N*M 형태로 놓인 숫자 카드가 있다.N은 행의 개수, M은 열의 개수를 의미한다. 
2. 먼저 뽑고자하는 행을 고른다.
3. 뽑은 행 안의 숫자들 중에서 가장 낮은 숫자를 선택한다. 
4. 이런 룰을 고려하여 가장 큰 숫자를 고를 수 있는 프로그램을 짜보자.
'''

# 조건 
'''
1<= N,M <= 100 
각 숫자는 1이상 10,000 이하
'''

# 입력예시 및 출력 
'''
3 3
3 1 2
4 1 4
2 2 2
=> 2 


'''

# 내 풀이 
import sys 

n,m = map(int,input().split())

min_num = [] # 가장 작은 숫자들을 담을 리스트 

for _ in range(n) : 
  lst_num = list(map(int,sys.stdin.readline().rstrip().split()))
  min_num.append(min(lst_num)) # 리스트 중 가장 작은 숫자를 배열에 담는다. 

# 가장 작은 숫자들이 모인 배열 안에서 가장 큰 숫자를 찾아서 출력 
print(max(min_num)) 


# 정답 코드 
n,m = map(int,input().split())

result = 0 
for _ in range(n) : 
  lst_num = list(map(int,input().split()))
  # 현재 행에서 가장 작은 숫자와, result 에 담긴 값을 비교해서 가장 큰 값을 다시 result 에 담는다. 
  result = max(result,min(lst_num))

# 가장 작은 숫자들이 모인 배열 안에서 가장 큰 숫자를 찾아서 출력 
print(result) 


