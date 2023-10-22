# 1316 - 그룹 단어 체커 

n = int(input())

count = n

for _ in range(n) : 
  group = input()
  for i in range(len(group)-1) : # 마지막까지 하면, 범위를 벗어나게 된다. 
    if group[i] == group[i+1] :  
      pass
    elif group[i] in group[i+2:]: # 포함된 것이 연속이 아닌, 다른 인덱스 위치에 포함되어있다면 
      count -= 1 # 그룹단어가 아니다.  
      break 

print(count) 
