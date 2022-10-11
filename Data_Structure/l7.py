names = ['MEENA', 'TEEENA', 'SEEENA', 'MANYA','TANYA']
first_letters = [ ]
last_letters = [ ]
for name in names :
    first_letters.append(name[0])
    last_letters.append(name[-1])

print(names)
print(first_letters)
print(last_letters)


#task
#creat list of short name from list of names

names = ['Project Manager', 'Central Processing Unit', 
            'Graphic card', 'Random access memory', 'input output']
short_name = [ ]
for name in names :
    short_name.sort(name)

