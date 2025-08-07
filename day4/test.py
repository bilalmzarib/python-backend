list1 = [1,2,3,4,5,6,7,8]

print(list1[::2])

list2=[]

for x in range(10):
    list2.append(x)

print(list2)

list2 = [x for x in range(10) if x%2 == 0]

print(list2)


tub = (1,2,3)

list3 = list1 + list2


dict1 = {"name":"naser", "age":1}
dict2 = {"major":"cs", "name":"mahmoud"}

dict3 = dict1 | dict2
print(dict3)
