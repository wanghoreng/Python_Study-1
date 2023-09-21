# 3052 번 

# 10 개의 수를 입력받아, 42로 나눈 뒤의 나머지들이 
# 서로 다른게 몇개 인지 출력하는 문제 

'''
42로 나눈 나머지들을 list 안에 넣어준다. 
그 담에 set 으로 형 변환을 하여 중복제거를 해준 뒤
set 안에 담긴 숫자들을 갯수 세는 방식으로 풀 예정 
'''

cnt_list = []
for i in range(0,10) : 
  a = int(input()) 
  x = a % 42  
  cnt_list.append(x)

answer = set(cnt_list)  
print(len(answer))     # len(obj) : 길이를 세주는 함수로 객체를 인자로 받는다. 