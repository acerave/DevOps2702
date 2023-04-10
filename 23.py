def print_pyramid(height):
    for i in range(2, height + 2):
        for j in range(1, height + 1):
            if j < i:
                print("$", end='')
        print()

print_pyramid(8)