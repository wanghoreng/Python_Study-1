# 주요 라이브러리 문법 

# 표준 라이브러리란 ?
'''
특정한 프로그래밍 언어에서 자주 사용하는 표준 소스코드를 미리 구현해놓은 라이브러리

파이썬 공식문서 에서 표준 라이브러리를 자주 확인하도록 하자. 
공식문서 : https://docs.python.org/ko/3/library/index.html 
'''

# 1. 내장 함수 : 프로그램 작성에 있어, 가장 기본적이면서 필수적인 기능을 포함하고 있는 함수/ 별도의 import 명령어 없이 사용가능하다. 
# 기본적으로, input(), print(), sum(), min(), max .. 등 이 있다.

# eval() : 수학 수식이 문자열 형식으로 들어오면, 해당 수식을 계산한 결과를 반환한다. 
print(eval("(3+5)*7"))

# sorted() : iterable 객체(반복가능한 객체)가 들어왔을 때, 정렬된 결과를 반환한다. 
# key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정할 수 있다. 
dic_sort = [('왕호랭이',98),('왕곰돌이',99),('그로밋',25),('징징이',26)]
print(sorted(dic_sort,key=lambda x:x[1])) # dic_sort 의 1번 인덱스 기준으로 정렬
# [('그로밋', 25), ('징징이', 26), ('왕호랭이', 98), ('왕곰돌이', 99)] 
print(sorted(dic_sort,key=lambda x:x[1],reverse=True))  # dic_sort 의 1번 인덱스 기준으로 내림차순 정렬 
# [('왕곰돌이', 99), ('왕호랭이', 98), ('징징이', 26), ('그로밋', 25)]

# sort() : iterable 객체는 기본적으로 정렬할 수 있는 함수를 내장하고 있다. 
arr = [9,4,5,1,3]
arr.sort() # 반환값은 None으로, 리스트 객체의 내부 값이 정렬된 값으로 변경된다. (sorted()는 내부값이 변경되진않는다.)
print(arr)
# [1, 3, 4, 5, 9]

# 2. itertools : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리 
# 기본적으로 순열과 조합에 대해서 다룬다. 

# permutations(=순열) : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해준다.
# 이를 순열이라고 한다.
from itertools import permutations 
per_data = ['A','B','C'] 
# result = permutations(per_data) # <itertools.permutations object at 0x10b78d350> 
# permutations 는 클래스 이므로, 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
result = list(permutations(per_data,3))
print(result) 
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations(=조합)) : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다. 
# 클래스이므로, 위와 똑같이 객체 초기화 이후 리스트 자료형을 반환한다. 
from itertools import combinations 
com_data = ['A','B','C']
result2 = list(combinations(com_data,3))
print(result2) 
# [('A', 'B', 'C')]  #순서를 고려하지 않기 때문에, 1,2,3 이든, 3,2,1 이든 123을 다른 순서로 배치해놨든 123이 들어있는 조합이기 때문에 1개의 경우의 수만 존재하는 것.

# product : permutations 와 같은 방식이지만, 원소를 중복하여 뽑는다. 
from itertools import product 
pro_data = ['A','B','C']
result3 = list(product(pro_data,repeat=2)) #product 는 repeat 속성값을 통해 뽑고자하는 데이터 수를 지정한다.
print(result3)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# combinations_with_replacement : combinations 와 같은 방식이지만, 원소를 중복하여 뽑는다. 
from itertools import combinations_with_replacement 
cwr_data = ['A','B','C']
result4= list(combinations_with_replacement(cwr_data,2))
print(result4)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')] 

# 3. math : 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리 
import math
print(math.factorial(5)) # factorial(x) : x! 의 값을 반환한다. 
# 120 -> 5!(5*4*3*2*1)
print(math.gcd(14,21)) # gcd(a,b) : a와 b의 최대공약수를 구하여 반환한다. 
# 7
print(math.sqrt(4)) # sqrt(x) : x의 제곱근을 구하여 반환한다. 
# 2.0
print(math.pi) # 파이(pi) 
# 3.141592653589793
print(math.e) # 자연상수 e 
# 2.718281828459045

