list1=[10,20,30, 41, 42]

new_list=[n+1 for n in list1]
print(new_list)

even_list=[n for n in list1 if n%2==0]
print(even_list)

odd_list=[n for n in list1 if n%2!=0]
print(odd_list)

letters=['a','b','c','d','e','f','g','h','i','o','p','q','u']
vowels_list=[letter for letter in letters if letter in ['a','e','i','o','u']]
print(vowels_list)


doubled_list=[num*2 for num in range(1,5)]
print(doubled_list)

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
four_letter_names=[name for name in names if len(name)<5]
print(four_letter_names)
upper_case_names=[name.upper() for name in names if len(name)>4]
print(upper_case_names)