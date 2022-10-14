a ={'ram','shyam','hari','gita','sita',}
b = {'eijha','klause','mark','bennny','sunny'}
c = {'ram','neha','sneha','urvi','surbi'}

#union
ab = a|b
print("union=>",ab)
#or
ab = a.union(b)
print("union=>", ab)

#intersection
ac = a & c
print('intersection=>',ac)

abi = a & b
print('intersection=>',abi)
ab = a.intersection(b)
print("union =>",ab)

#difference

ac = a-c
print("diffrenece =>",ac)

ca = c-a
print("diffrence =>",ca)

#symmetric diffrence

ac = a ^ c
print("symmetric diffrence",ac)
