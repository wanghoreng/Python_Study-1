# 2098 - 상수 

a,b = input().split()
a = ''.join(list(reversed(a)))
b = ''.join(list(reversed(b)))

if (int(a) > int(b)) : 
  print(a)
else : 
  print(b)

# 다른 사람 풀이 
a,b = map(str,input().split())
num = []
num.append(a[::-1])
num.append(b[::-1])
print(max(num))
