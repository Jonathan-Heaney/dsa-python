# Even though this is n^2 + n, we drop n because it's non-dominant
# Anything that's below the highest O complexity gets dropped

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)
