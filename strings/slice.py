s = 'digipodium'
slice1 = s[3:8]
print(slice1)

m = 'This is an example'
print(len(m))
for i,v in enumerate(m) :
    print(f'{i} - - > {v}')

    #sliceing
    print(m[5:7])
    print(m[8:10])
    print(m[11:18])


s = 'digipodium'
slice1 = s[0:4]
slice2 = s[:4]
print(slice1)
print(slice2)

slice3 = s[4:len(s)]
slice4 = s[4:]
print(slice3)
print(slice4)

print(s[-6:])
print(s[-7:])

rr = '1,1111 rating | 452 answered question'
print(len(rr))
for i,v in enumerate(rr) :
    print(f'{i} - - > {v}')

print('total answers' , rr[16:])


