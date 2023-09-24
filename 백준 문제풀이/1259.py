# 1259번 문제 

# 팰린드롬수에 대한 문제 
# 팰린드롬 : 어떤 단어를 뒤에서부터 읽어도 같은 단어 

# 내가 한 방식에서 reverse 를 했더니 
# 복사한 변수도 똑같이 적용되는 문제 -> 얕은 복사로, '참조'만 복사한다는 것을 발견/ 같은 곳을 참조해서 객체를 변경하면 같이 변경되는 것 

import copy # copy함수를 쓰기 위해서 copy 모듈 import 해주기 

while True : 
  n = int(input())
  if n == 0 :  
    break
  else : 
    list_n = list(map(int,str(n)))
    #real_listN = list_n # 얕은 복사(=,대입연산자 뿐만 아니라, copy()함수, [:] 슬라이싱 도 얕은복사에 해당한다)
    real_listN = copy.deepcopy(list_n) 
    # copy.deepcopy 는 완전한 깊은복사함수이다. 
    list_n.reverse() 
    if real_listN == list_n : 
      print('yes')
    else : 
      print('no')


# 다른 사람 풀이 확인해보니 
# 처음부터 끝까지 거꾸로 비교하는 것을 슬라이싱으로 하면 된다 
n = str(163)
print(n[::-1]) #361 -> 숫자는 슬라이싱이 불가능하다. 
# 문자열은 배열처럼 슬라이싱을 사용할 수 있다 

while True : 
  n = input()
  if n == "0" : 
    break
  elif n == n[::-1] : 
    print('yes')
  else :
    print('no') 
    