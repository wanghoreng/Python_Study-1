# 25206 - 너의 평점은

dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5,'B0':3.0,'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0,'F':0.0}

# 학점 총합
sum = 0
# 학점 * 과목평점 합
result = 0 

for _ in range(20) : 
  sub,score,grade = input().split()
  if grade == 'P':
    continue
  else : 
    result += float(score) * dic[grade]
    sum += float(score)

print(f"{result / sum:.6f}")
  
  