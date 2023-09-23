# 2231번 문제 

'''
M 의 분해합이 N 인 경우, M 을 N 의 생성자 
분해합 : N + N 을 이루는 각자리의 합 
ex : 125 의 분해합 : 125 + 1 + 2 + 5 = 133 즉, 133의 생성자가 125이다. 

2자리 숫자면 분해합과정 (xy + x + y) = 이 과정에서 xy 가 저 합의 생성자. 
3자리 숫자면 분해과정 (xyz+...)

어렵게 생각할게 아닌, for 문으로 처리하면 되는 것이였다.
'''

print(list(str(1))) 
# ['1']
print(list(str(10))) 
# ['1', '0'] 
# print(list(10)) 
# iterable 반복가능한 객체가 아니기때문에 list 가 안만들어짐
# 'int' object is not iterable 에러 발생. 
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 문제풀이 
n = int(input())

# 1부터 입력값(즉, 분해값)까지 반복문 돌리기 
for i in range(1,n+1) : 
  # 숫자형으로 리스트에 담아주기
  # list 안에 문자열로 형변환한 후 int 로 바꾸는 이유는 
  # list 로 형변환할 때 2자리 수 이상 들어가기 시작했을때 문자열로 넣게 되면 한자리수 처럼 들어가기 때문이다, 
  arr = list(map(int, str(i)))
  #print(arr) # 확인
  # 배열에 담긴 값을 다 합치고, i 자체를 더하기 
  # 분해 과정에서는 각자리 수를 합치는 과정이 sum(arr)
  # 생성자 더하는 과정이 i 
  result = sum(arr) + i 
  if(result == n) : 
    print(i) 
    # 가장 작은 생성자만 구하기 위해 break, 안할 경우 여러개 생성자 나옴 
    break
  # 생성자와 분해핪이 같다면, 생성자가 없다는 것과 같다. 
  elif (i == n) :
    print(0)
