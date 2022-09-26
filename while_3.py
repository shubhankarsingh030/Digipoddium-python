total = 0

while 1:
    num = input("Enter a number")
    if not num:
        break
    if num.isnumeric():
        total += int(num)
    print(f"total => {total}")