#generate a list of prime nunber less than a given nummber 
number = 10
a = [i for i in range(2,number) if all(i%j!=0 for j in range(2,i))]
print(a)

# create any set anf try to use frozenset(setname)

# Find the elements in a given set that are not in another set

#     set1 = {1,2,3,4,5}
#     set2 = {4,5,6,7,8}

#     diffrence between set1 and set2 is {1,2,3}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
frozenset(set1)
frozenset(set2)
result = set1.difference(set2)
print(result)
print(set2.difference(set1))
print(set1.add(frozenset(set2)))
print(set1)
print(set1.update(set2))
print(set1)