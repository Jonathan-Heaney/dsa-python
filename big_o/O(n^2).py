# Quadratic, loop within a loop
# This is a horrible big O, avoid this whenever possible. It grows very fast with large numbers

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(10)
