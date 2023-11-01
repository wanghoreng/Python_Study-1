# 2720 - 세탁소 사장 동혁 

t = int(input())

money = [25,10,5,1]

for _ in range(t) :
  coin = [0,0,0,0]
  c = int(input())
  for i in range(len(money)) : 
    if c >= money[i] : 
      coin[i] = c//money[i]
      c = c % money[i] 
  for i in coin : 
    print(i, end=' ')
  print()


