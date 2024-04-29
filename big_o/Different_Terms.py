# Since there are 2 different inputs, you can't just say the time complexity is O(n). The best you can do is O(n + m)

def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


print_items(1, 10)
