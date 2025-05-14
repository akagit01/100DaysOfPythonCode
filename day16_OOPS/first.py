print("hello hello bhailog")
length=5
for i in range(5):

        print (f'count {i}')


num=0
while (num < length):

        print(f'num is {num}')
        num+=1

list1=['chiku','apple', 'banana', 'guava']
for i in list1:
    print(i)

#cnt=list1.count()
#print(cnt)
print(len(list1))
list1.sort()
print(list1)
list1.append('dates')
print(list1)
list1.sort()
list1.insert(5,'eggs')
list1.sort()
list1.reverse()
print(list1)

set1={12,13,14,55,22,13}
print(set1)
#print(set1.count(13))



dict1={'name':'aka','age':12,'city':'dubai'}
print(dict1.values())
print(dict1.get('name'))
print(dict1.keys())
print(dict1.items())
print(dict1.pop('name'))
print(dict1.items())


