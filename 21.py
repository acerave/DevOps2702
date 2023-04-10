numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finished successfully")