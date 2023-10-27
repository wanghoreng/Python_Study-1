# 10798 - 세로 읽기 

# 문제 요약 
'''
한줄에 최대 15개를 입력받을 수 있는 단어를 5개 만든다 
단어의 갯수는 서로 다를 수 있다. 
총 5개의 단어를 세로로 읽은 순서대로 글자들을 출력한다.
세로로 읽을 단어가 없을 경우, 다음 줄을 읽는다. 
'''

str_lst = []

for _ in range(5) : 
  str_line = input() #문자열 
  str_lst.append(str_line)

for i in range(15) : 
  for j in range(15) : 
    try : 
      print(str_lst[j][i],end='')
    except : # list out of range 예외 처리  
      pass


# 다른 사람 풀이 

text = [input() for _ in range(5)]

for i in range(max(len(e)) for e in text) # text 중 가장 긴 문자열만큼 
  for j in range(5) : # 열 (단어의 갯수 총 5개)
    if i < len(text[j]) # 글자수체크(i)보다 text[j] 길이가 짧으면 text[j]의 i 번째가 없다는 뜻이기 때문에, 작을 경우에만 출력한다. 
      print(text[j][i], end='')

