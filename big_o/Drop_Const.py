# Even though there are 2 for loops here, it's the same big O, O(n)
# It's n operations twice. n + n = 2n. We drop constants in big O, so O(2n) == O(n)

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)
