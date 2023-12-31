# 11399 - ATM 문제 

# 그리디 알고리즘 : 미래를 고려하지 않고 현재상황에서 선택한 것이 최적의 해를 보장한다고 생각하는 것 

# 문제풀이 방식
'''
해당 문제는 주어진 배열에 있어서 앞의 인덱스번호를 기다리는 시간을 
누적시키는 형식으로 주어져 모든 인덱스 번호의 기다리는 시간을 최소합으로 
구하는 문제이다. 

그렇다면 앞에서 누적되는 시간이 최소값이려면 
자신보다 작은 숫자들이 누적되어야 최소값을 만들 수 있다. 
그래서 오름차순으로 정렬해준 뒤 누적시켜주는 방식으로 해결하였다. 
'''

# 내풀이 

# 사람 수 입력
n = int(input())
# 각 사람 수의 시간 입력 
time = list(map(int,input().split()))

# 작은 순으로 정렬 
time.sort()

# 앞 사람 시간을 누적 
# 1 2 3 3 4 
# 1 1+2 1+2+3 
# time[0]  time[0]+time[1]  time[0]+time[1]+time[2]
for i in range(1,len(time)) : 
  time[i] += time[i-1]

print(sum(time))



# 다른 사람 풀이 
n = int(input())
time = list(map(int,input().split()))
time.sort() # 오름차순 정렬 

# 누적합 변수 
result = 0 

for i in range(n) : 
  result += time[i]*(n-i) 
print(result)
'''
숫자리스트[i번째]*(총 숫자 - i) 으로 첫번째 수 * 반복되는 만큼 식을 세웠다. 
해당 풀이를 확인해보니, 
3 + (3+1) + (3+1+4) + (3+1+4+3) + (3+1+4+3+2) 라는 해설을 자세히보면 
첫번째 수 3 이 다른 숫자에 더해지는 것을 반복하는 횟수가 총 5번임을 알 수 있다. 이를 계산하여 저런 식이 나오게 된 것이다. 
=> time[i]*(n-i) 
'''


