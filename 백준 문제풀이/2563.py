# 2563 - 색종이 

# 문제 접근 방식
'''
색종이가 가로 1, 세로 1인 작은 정사각형 100개로 이루어졌다고 가정한 후,
도화지에 색종이가 붙은 검은 영역을 1로 채워주고 
이에 값이 1인 칸의 개수만 count 하면 검은 영역의 면접을 구할 수 있다. 
'''

# 도화지 범위 초기화 (가로,세로 각각 100)
paper = [[0 for _ in range(100)]for _ in range(100)]

for _ in range(int(input())) : 
  x,y = map(int,input().split()) # 왼쪽 순, 아래 순으로 x,y 좌표를 받는다. 
  for i in range(x, x+10) :  # 가로 순으로 돈다.
    for j in range(y, y+10) :  # 세로 순으로 돈다 
      paper[i][j] = 1 

# 1로 채워진 영역을 카운트 한다. 
count = 0 

# 방식 1 
# for x1 in range(100) : 
#   for y1 in range(100) : 
#     if paper[x1][y1] == 1 : 
#       count += 1

# 방식 2 
# paper 의 row를 읽음
for count_n1 in paper : 
  count += count_n1.count(1) # 그 row 중 1 숫자가 들어있는 것을 영역을 카운트 

print(count)
