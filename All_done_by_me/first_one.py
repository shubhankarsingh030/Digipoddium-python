#1.Creat a string and print it.

my_string = "I can do this all day"
print(my_string)

#2.Take a string inpute and prints length.

sentence = """Python is a computer programming language often used 
to build websites and software, automate tasks, and conduct data 
analysis.Python is a general-purpose language, meaning it can be 
used to create a variety of different programs and isn't specialized 
for any specific problems"""

chars = len(sentence)
print(f'Total character:{chars}')


#3.Print the last word of the string "Python is great" using slice

sen = "Python is Great"
chars = len(sen)
print(f'total character:{chars}')
slice = sen[10:]
print(slice)
#by splitting
last_word2 = sen.split()[-1]
print(last_word2)

#4.print each in word in diffrent line string "Pyhton is everywhere"

s = "Python is everywhere"
print(len(s))
for word in s.split():
    print(word)

#5.print the string "Hello world" in reverse.

m = "Hello world"
print(m[::-1])

