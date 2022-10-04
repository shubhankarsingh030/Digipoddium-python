#getting a list slice

l = [10,20,30,40,50,60,70,80,90,100]
slice1 = l[3:-2]
print(slice1)
slice2 = l[-6:-1]
print(slice2)



#append function

fruits = []
fruits.append("banana")
fruits.append("apple")
fruits.append("cherry")
fruits.append("guava")
print(fruits)

fruits.insert(1,"orange")
print(fruits)

fruits.insert(0,"papaya")
print(fruits)

vegetables = ["dhaniya", "mirch","alloo","began"]
fruits.extend(vegetables)
print(fruits)
fruits.append(vegetables)
print(fruits)
fruits.remove(vegetables)
print(fruits)
fruits.remove("dhaniya")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.reverse()
print(fruits)



