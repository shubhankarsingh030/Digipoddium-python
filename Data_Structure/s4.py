#clean a list of a duplicate values

x = [1,1,1,2,4,5,56,7,7,6,868,566,4,54]
print(x, 'duplicated values')

x = list(set(x))
print(x, 'cleaned sheet')

#data structure conversion

x = [1,2,3,4,5]
print(x, 'list')

x = tuple(x)  #convert list to tuple
print(x, 'tuple')

x = set(x)  #convert tuple to set
print(x, 'set')

x = list(x)  #convert set to list
print(x, 'list')

