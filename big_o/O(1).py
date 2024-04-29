# There's a defined number of operations that doesn't depend on the inputs
# Whether that number of operations is 1 or 1000 is irrelevant, it's still O(1) complexity, which is the most efficient big O

def add_items(n):
    return n + n + n


print(add_items(10))
