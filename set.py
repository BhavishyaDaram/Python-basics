# a = {1,2,3,4}
# a.remove(2)
# a.add(7)
# a.pop()
# a.clear()#removes all the elements
# print(a)

# meathods
a={1,2,3,4,5}
b={4,5,6,7,8}
s= a.union(b)#a|b
k=a.intersection(b)#a&b
r=a.difference(b)#a-b
o=a.symmetric_difference(b)#a^b
b-=a
print(s)
print(k)
print(r)
print(o)
print(b)