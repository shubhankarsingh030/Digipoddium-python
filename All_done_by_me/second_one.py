#6.Convert the string "How are you?"" in uppercase

msg = "how are you?"
result = msg.upper()
print(result)

#7.Convert the string How Is It Going? in lowercase.

msg1 = "How Is It Going?"
result = msg1.lower()
print(result)

#8.Join the following list by spaces( ) and print the result:
# words = ['Python', 'is', 'easy', 'to', 'learn']

words = ['Python', 'is', 'easy', 'to', 'learn']
result1 = " ".join(words)
print(result1)
result = result1.upper()
print(result)


#9.Print a multiline string using a single print

data = '''dbjebuaewcub rfaeicuie gcuae cuer uygra e
uc earucbeubvu erbcu aebyv ueabvuear'''
print(data)


#10. Print this string "to move to newline'\n' is used". 
# (results should look exactly like the provided string)

msg = r"to move newline '\n' is used" #r is used for raw string

print(f'this is the result:{msg}')

#11.Print a variable with some text using a single print function, output should look like following.

msg2 = "the varibale is 15"

print(msg2)

#12. concatenate the following strings and print the result
s1 = 'python '
s2 = 'is '
s3 = 'great.'

merged_string = s1+""+s2+""+s3

print(merged_string)

#13.Print # 20 times without using a loop

lines_20 = ("20\n" * 20)

print(lines_20)

#14.Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-

for i in range(1,9):
    print(f'{i}.')


