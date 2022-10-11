from dataclasses import dataclass


num = []
for i in range(10):
    data = input("enter yoy number:")
    if data.isnumeric():
        num.append(int(data))

print("your data =>",num)