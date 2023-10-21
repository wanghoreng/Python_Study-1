# 5622 - 다이얼 문제 

# 2 ~ 9 
# index + 2(인덱스차이) + 1(시간초)
eng_lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

str_lst = input() 

arr = []
# 입력문자를 한 문자씩 반복문을 돌린다. 
for s in str_lst :  
  # 문자가 담긴 문자열 안에, 입력문자를 가진 문자가 있는 인덱스를 반환한다. 
  arr += [i+3 for i in range(len(eng_lst)) if s in eng_lst[i]]

sum = 0

for a in arr : 
  sum += a 
print(sum)




