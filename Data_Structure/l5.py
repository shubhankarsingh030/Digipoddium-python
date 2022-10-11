x =[]

for i in range(10):
    data = input('enter float value:')
    if '_' in data and data.count('.') == 1:
        p1,p2 = data.split('.')
        if p1.isnumeric() and p2.isnumeric():
            x.append(float(data))
    if data.isnumeric():
        x.append(float(data))
print(x)