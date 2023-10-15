# 25314 - 코딩은 체육과목입니다. 문제 

# 문제 접근 방식
'''
n 이 4의 배수여서 n을 -4 로 빼주면서 
더 이상 뺄 수 없을 때 까지 반복문 돌려서 
long 을 붙일 생각이었다. 
반복문 분류에 있던 문제여서 반복문을 돌리는 문법만 고려했었는데 
다른 사람 풀이를 보고 나니,
조금 더 수학적으로 고려를 해보는 걸 노력해봐야겠다. 
'''
n = int(input())

str = 'long'
if (n==4) : 
  print(str,'int')
else : 
  while n > 4 : 
      str += ' long'
      n -= 4 
  print(str,'int')

# 다른 사람 풀이 
n = int(input())

# 4 의 베수여서 그냥 몫을 구한 뒤 long 을 그만큼 곱해주면 되는 풀이
str = 'long ' * (n//4)
print(str +'int') 
# 쉼표(,) 로 문자열을 이어주면 공백이 생기므로 두칸 공백으로 인해 오답이돼서 문자열 덧셈 연산을 이용