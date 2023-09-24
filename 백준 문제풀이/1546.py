# 1546 번 문제 

# 평균 구하는 문제이지만, 출력값의 절대오차 또는 상대오차가 
# 10의 -2제곱 이하여야 정답인 문제

'''
그냥 평균구하듯이 풀어서 맞췄당 
'''

T = int(input())
score = list(map(int,input().split()))
sum = 0 
for i in range(len(score)) : 
  sum += score[i]/max(score)*100
print(sum/len(score))