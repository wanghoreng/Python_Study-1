# 10814번 문제 

# 나이순으로 정렬하는 문제, 같은 나이라면 가입한 순서대로 정렬

'''
가입한 순서대로 미리 주어지므로, 
같은 나이일 때 정렬하는 것은 생각 하지않아도 될것같고, 
나이순은 숫자 작은 것부터 큰 순으로 정렬하면 될것같다.
딕셔너리로 한번 받아보자 -> 굳이 딕셔너리가 아닌, 2차원 리스트로 만들어서
사용이 가능했다. 
'''
import sys


lst_logs = [] 
for i in range(int(input())) : 
  #lst_log = input().split() 
  lst_log = sys.stdin.readline().split()
  lst_log[0] = int(lst_log[0])
  lst_logs.append(lst_log)
# print(lst_log)
# [['21', 'kim'], ['21', 'ji'], ['20', 'hea']]



lst_logs.sort(key=lambda x : x[0])
#print(lst_log) # [['21', 'bac'], ['20', 'aaa'], ['21', 'abc']]
#print(lst_log2) # [['20', 'aaa'], ['21', 'bac'], ['21', 'abc']]

for log in lst_logs : 
  print(log[0], log[1])

# 알게된 것 
'''
lambda 인자리스트 : 표현식 
나는 처음에 람다 뒤에 나오는 인자리스트부분은 선언된 변수만을 가져다가
넣어야하는 줄 알았는데, 인자리스트라는 곳에 변수선언하듯이 이름을 붙이면 되는 것이었다. 
'''
# lst_logs.sort(key=lambda x : x[0])
'''
그래서 이 뜻은 
lst_logs 의 [0]번째 인덱스 를 기준으로 정렬하겠다는 의미이다. 
여기서 x 는 lst_logs 리스트를 가리키는 것인데 이게 가능한 이유가 
sort 정렬이 반복적인 객체에서 인덱스마다 값을 꺼내서 키를 기준으로 정렬하겠다는 의미이기 때문이다. 
'''

# sys.stdin.readline()
'''
입력받는 속도가 너무 느려서, 알아본 함수로 
반복문을 여러줄 입력받을 때 input() 함수는 시간초과가 발생한다고 해서 
사용된 함수이다. 

특징 )
이 함수는 한줄 단위로 입력을 받으며, 개행문자가 같이 입력받아진다. 
변수 타입이 문자열 형태이기 때문에, 정수 사용을 원한다면 형변환을 거쳐야한다. 
'''