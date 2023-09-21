# 2577번 문제 

# 자연수 3개를 입력받아 3개 다 곱한 뒤 0 ~ 9 까지 숫자가 각각 몇번 쓰였는지 
# 구하는 문제 

'''
곱해진 값을 문자열로 처리하여 
0~9까지 반복문을 돌려서 값을 찾을 예정 
'''


A = int(input())
B = int(input())
C = int(input())
# str() : 숫자를 문자로 변환시켜준다. 
xsum = str(A*B*C)

# 내풀이 
for j in range(0,10) : 
    if(xsum.find(f'{j}') != -1) :   # find(str) : 찾는 글자가 있으면 인덱스 반환, 없으면 -1 반환 
      print(xsum.count(f'{j}'))   
    else :
      print(0)

# 다른 사람 풀이 -> 생각해보니, count() 함수는 없으면 그냥 0 반환하는 거였다.. ㅎ 
for i in range(0, 10) : 
   print(xsum.count(str(i)))




