# 2941 - 크로아티아 알파벳 문제

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n = list(input())
# 크로아티아 알파벳이 아닌 문자 담는 공간
arr = n[::] 

#전체 알파벳 세는 변수 
count = 0
# 입력리스트 인덱스 
i = 0 

while i < len(n)-1 : 
  if ''.join(n[i:i+2]) in croatia : # 크로아티아 리스트에서 입력받은 문자 2개 중 같은게 있다면 
    arr.remove(n[i])   # 크로아티아 알파벳 지워주기 
    arr.remove(n[i+1])
    i += 2 
    count += 1
  elif ''.join(n[i:i+3]) in croatia : # 크로아티아 리스트에서 입력받은 문자 3개중(dz=) 같은게 있다면 
    arr.remove(n[i])    # 지워주기 
    arr.remove(n[i+1])
    arr.remove(n[i+2])
    i += 3
    count += 1 
  else : 
    i += 1 
# 크로아티아 알파벳이 아닌 알파벳 갯수와 크로아티아 알파벳 갯수 더해주기 
print(len(arr) + count)


# 다른 사람 풀이 
word = input()

for i in croatia : 
  word = word.replace(i,'*') # 입력받은 문자에서 크로아티아 문자를 별표로 변경한다. 
print(len(word))
'''
replace() 함수 : 문자열을 변경하는 함수이다. 
문자열안에서 특정 문자를 새로운 문자로 변경하는 기능을 가지고 있다. 
문법 : replace(old,new,[count]) 형식 
- old : 현재 문자열에서 변경하고 싶은 문자 
- new : 새로 바꿀 문자
- count : 변경할 횟수 
'''