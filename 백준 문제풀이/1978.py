# 1978 번 문제 

# 입력값의 소수의 개수를 찾는 문제다 

# 소수란, 약수가 1과 자기자신 뿐인 숫자를 말한다. 
# 예를 들어, 1 을 제외한 2 3 5 7 11 13 .. 



N = int(input())
num = list(map(int,input().split()))
sum = 0  # 소수의 개수 세어주는 누적변수 
for i in range(len(num)) :   # 리스트의 길이까지 반복문 돌려준다. 
  if (num[i] != 1) :         # 리스트의 값이 1이 아닐경우에만 조건식에 들어간다. 
    num_cnt = [1,num[i]]     # 소수의 조건인, 1과 자기자신 값이 들어간 리스트를 하나 만든다.  
    cnt = []                 # num_cnt 배열과 같으면 소수인 것으로 확인하기 위한 빈배열 
    for j in range(1,num[i]+1) :   # 원래 여기서(1,101)까지로 했었는데, 생각해보니 자기자신까지만 나눠보면 된다. 
      if(num[i] % j == 0) :        # 리스트의 값과 j 를 나눈 나머지가 0 일경우 
        cnt.append(j)   # 아까 그 빈 배열에 넣어준다.
    if(num_cnt == cnt) :   # 그리고 아까 num_cnt 와 비교해서 맞다면 
      sum += 1             # 소수의 개수 세어주기 
print(sum)

# 다른 사람 풀이를 보니, 더 간단한 방식으로 풀 수 있었다. 
# 그냥 1과 반복문 돌리는 num 값을 제외한 2 부터 num-1 값까지 나눈 몫이 0 이면 #
# 소수가 아닌 것이고, 나머지가 0인값이 없다면 소수인 것으로 방식을 바꿔 해결할 수도 있었다.

N = int(input())
num = list(map(int,input().split()))
sum = 0
for i in num :   # 여기서 처음 안 사실, 리스트여도 num만 으로 표현가능한데, 이 때 i 는 num 의 값이 순서대로 나온다. 
  error = 0       
  if i > 1 :     # num 의 값이 1보다 클 경우 
    for j in range(2,i) :   # 2 부터 n-1 까지 
      if(j % i == 0) :      
        error += 1         # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
    if error == 0 :        # error가 없으면 소수.
      sum += 1 
print(sum)
    

