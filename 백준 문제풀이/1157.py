# 1157 번 - 브론즈 1 문제 

# 가장 많이 사용된 문자를 찾는 문제 

#1. 입력받기 -> 예시) Mississipi 
str = input()
#2. 대소문자 구분없이 문자를 비교하기 위해 lower() 함수로 전체 문자를 소문자로 바꿔줌 
# 꼭 lower() 함수가 아니라, upper() 함수도 가능! 
str = str.lower() 
# 3. set 하여, 중복제거 한 뒤 list 로 바꾼 것 
str_list = list(set(str)) 

# 4. 중복제거된 문자의 개수를 각각 배열에 담아주기 위한 빈 배열 만들기
cnt_list = []

# 5. 중복제거된 문자리스트를 반복문 돌리기 
for i in str_list : # m i s p 
  # 6. 해당 문자의 개수를 변수에 담는다.
  str2_iNum = str.count(i)    
  cnt_list.append(str2_iNum) # 그 변수를 아까 만든 빈배열에 넣는다. 
  # print(cnt_list)          # 반복문을 총 돌렸을 때 이 배열은 [1,4,4,1] 또는 다른 1 이 2개, 4가 2개인 순서가 뒤죽박죽인 배열이 만들어진다. -> 이 이유는 set 이 순서는 보장되지 않기 때문이다. 

  # 7. max(cnt_list) : 해당 리스트에서 가장 큰 값 (예시 : 4) 이 cnt_list 에서 count 로 몇 개인지 확인하는 조건식으로 큰 값이 1개보다 많을 경우 
if (cnt_list.count(max(cnt_list)) > 1) : 
  print('?')
else :  # 8. 큰 값이 1개거나 0개 일경우 -> 예시 입력이 만약 baaa 일 경우 , cnt_list = [1,3] 또는 [3,1]
    #print(cnt_list.index(max(cnt_list))) 
    # 9. cnt_list 안에서 가장 큰 값(예시 : 3) 으로 cnt_list 에서 가장 큰 값의 인덱스를 찾은 뒤, 
    #    str_list(baaa 예시로는 [b,a] 또는 [a,b]) 의 인덱스로 문자를 찾은 뒤, 그 문자를 upper() 함수를 통해 대문자로 출력한다. 
    print(str_list[cnt_list.index(max(cnt_list))].upper())


# 이 문제를 통해 알게된 함수 
# upper() : 대문자로 만들어주는 함수 
# lower(): 소문자로 만들어주는 함수 
# list.index(ch) : 리스트 안의 값으로 그 값이 해당 리스트에서의 인덱스 위치를 반환하는 함수 
# max(iterable) : 매개변수로 들어온 인자내부에서 제일 큰 값을 반환한다. 
# -> 반복가능한 자료형들 중 가장 큰 값을 찾는 함수 

                
