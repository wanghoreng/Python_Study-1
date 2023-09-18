# 2023/09/18

# 튜플은 수정, 삭제, 추가가 불가능하지만 이를 가능하게 하는 방법이 존재한다. 
my_tuple = ('오예스', '몽쉘')
my_list = list(my_tuple)
my_list.append('초코파이')
my_tuple = tuple(my_list)
# 튜플 <-> 리스트 를 하고 싶을 경우, 튜플(), 리스트() 를 해주면 변환이 가능하다. 


# 리스트에서 중복을 제거하고 싶을 때 
my_list2 = ['오예스','몽쉘', '초코파이', '초코파이', '초코파이']
my_set = set(my_list2)
my_list2 = list(my_set)
# set 으로 변환했다가 다시 리스트로 변환해주면 중복이 제거된다. 
# 하지만 set 은 순서가 보장되지 않기 때문에 set으로 변환 후 다시 리스트로 왔을 때 순서가 뒤바껴져있을 수 있다. 

# 이 경우에는 딕셔너리를 사용해주면 된다. 
my_list3 = ['오예스','몽쉘', '초코파이', '초코파이', '초코파이']
my_dic = dict.fromkeys(my_list3) # 리스트를 변환해주는 함수
print(my_dic)
# {'오예스': None, '몽쉘': None, '초코파이': None}
my_list3 = list(my_dic)
print(my_list3)
# ['오예스', '몽쉘', '초코파이']

