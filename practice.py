# commit test 2
a = '안녕 왕호랭이야' 
print(a.startswith('안녕')) 
#startswith(문자열) => bool 타입 반환 : 첫글자가 괄호안의 문자열과 같다면 True, 아니면 False 를 반환, 앞에 공백이 있는 것도 포함
print(a.endswith('왕호랭이야'))  
#endswith(문자열) => 끝글자가 괄호안의 문자열과 비교하여 불리언 타입 반환 
print(a.strip()) # a.strip(' ') 과 같은 결과를 출력함 
#strip(제거하고 싶은 문자열 또는 공백) => 앞뒤로 제거하고 싶은 문자열을 제거해준다.  
print(a.replace('왕호랭이','왕곰돌이'))
# replace('바꾸고싶은문자열','바꾼문자열')
print(a.find('왕')) 
# find('찾고싶은문자열') => 해당 문자를 찾아 인덱스를 반환
print(a.center(13,'@'))
# center(문자열길이,'넣고싶은문자') => 변수에 담긴 문자열길이에서 넘겨준 문자열길이의 빈칸에 넣고싶은 문자가 들어간다. (문자열은 안됨)
# ==> @@안녕 왕호랭이야 @@

#문자열 합치기 (,) 로 합칠 수 있다! => 자동 띄워쓰기가 되면서 합쳐진다. 
a1 = 'hello'
a2 = 'wang ho reng'
print(a1,a2) 

#문자열 포맷 
# 1.
print('안녕 {} {} 이야.'.format(a1,a2))  
# 2. 
print('안녕 {1} {0} 이야.'.format(a1,a2))  
# 3.
print(f'안녕 {a1} {a2} 이야.')  

# 리스트 
'''
리스트명 = [] 
처럼 만들어주면 된다. 
특징)
1. 괄호안은 비어있을 수 있다. 
2. 데이터타입이 같을 필요가 없다.
3. 중복된 데이터가 들어가도 가능하다.  
4. 순서 보장! 
'''


my_list = ['one','two','three']
# 리스트에 문자열 추가
my_list.append('four')
print(my_list)
# ['one', 'two', 'three', 'four']

# 리스트 제거 
my_list.remove('two')
print(my_list)
# ['one', 'three', 'four']

# 리스트 끼리의 확장 
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(my_list)
# ['one', 'three', 'four', 1, 2, 3]

# 튜플 
'''
튜플명 = ()
구분은 콤마로 가능하다. 
특징)
1. 리스트와 거의 비슷하다.(= 읽기 전용 리스트)
2. 한번 값을 넣고나면 수정이 불가능하다. 
3. 순서가 보장된다. 
4. 중복 허용. 
'''

# 튜플만의 특징! 
'''
패킹 : 오른쪽의 값들을 왼쪽 튜플변수에 집어넣는다. 
언패킹 : 튜플변수명에 담긴 값들을 꺼내서 변수에 저장하는 것을 말한다. 
'''
# 패킹
tuple1 = ('난','튜플','이지롱','메롱메롱')
# 언패킹
(a,b,*c) = tuple1
# 여기서 * 이 붙은 변수는 튜플에 담긴 순서대로 변수의 첫번째부터 하나하나씩 저장이 되는데, 
# 그 중 저장이 안된 나머지 변수 모두를 * 이 붙은 변수리스트에 넣는다는 의미.
# 이 때 값이 여러개이기 때문에 *이 붙은 변수에 들어간 값들은 리스트 형태로 들어가게 된다. 
print(c)
# ['이지롱', '메롱메롱']


# 세트(set) 
'''
세트명 = {}
특징)
1. 순서 보장하지 않는다. 
2. 중복 허용하지 않는다. 
3. 인덱스로는 접근이 불가능하다. => 순서가 없기 때문. 
'''

set1 = {'돼지고기','삼겹살','제육덮밥'}
set2 = {'삼겹살','갈비','아이스크림'}
# 교집합 
print(set1.intersection(set2))
# {'삼겹살'}

# 차집합 
print(set1.difference(set2))
# {'제육덮밥', '돼지고기'}

# 합집합
print(set1.union(set2))
# {'삼겹살', '갈비', '아이스크림', '제육덮밥', '돼지고기'}

# 값 집어넣기
set1.add('고르곤졸라') 
print(set1)
# {'돼지고기', '고르곤졸라', '제육덮밥', '삼겹살'}

# 값 제거하기
set2.remove('아이스크림') 
print(set2)
# {'갈비', '삼겹살'}

# set 안의 값들을 모두 없애기 => 리스트, 튜플, 딕셔너리 도 같다. 
set1.clear()
print(set1)
# set()

# set 자체를 삭제 => 이건 리스트, 튜플, 딕셔너리도 가능하다.
del set2 
#print(set2)
# NameError: name 'set2' is not defined. 


# 딕셔너리
'''
딕셔너리명 = {key1:value, key2:value2 ...}
1. value 값은 데이터 타입 상관없다. 
2. key 값은 중복을 피해야한다. 
'''

person = {
  '이름' : '왕호랭이'
  ,'나이' : 26
}
print(person['이름']) # 왕호랭이
# get
# print(person['주소']) # 에러 -> person 에 주소라는 키가 존재하지 않기에 에러가 뜬다. 
print(person.get('주소')) # None -> get 을 이용한다면, 에러가 아닌 none 을 반환한다는 차이점을 기억하자. 

# 키와 값 추가 
person['주소'] = '비밀'
print(person)
# {'이름': '왕호랭이', '나이': 26, '주소': '비밀'}
# 수정도 위와 같이 해주면 되지만
# 여러 값을 바꾸고 싶을 때 
person.update({'이름':'왕곰돌이','나이':25})
print(person)
# {'이름': '왕곰돌이', '나이': 25, '주소': '비밀'}

# 키 삭제 
person.pop('주소')
print(person.keys())
# dict_keys(['이름', '나이'])
print(person.values())
# dict_values(['왕곰돌이', 25])
print(person.items())
# dict_items([('이름', '왕곰돌이'), ('나이', 25)])
