# 1152 번 - 브론즈 2 문제 
str = input().split()  # 공백을 기준으로 구분하여 배열에 담는다. 
# The last character is a blank -- 입력(글자 사이사이 공백이 구분자가 된다.)
print(len(list(str))) 
# 6 

# 메모리 : 	39196kb
# 시간 : 56ms

# 다른 사람 풀이 
str = list(input().split()) # 이렇게 바로 할 수도 있구나.. 
print(len(str))