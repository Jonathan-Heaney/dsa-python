num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)  # 11
print("num2 =", num2)  # 11

print("\nnum1 points to:", id(num1))  # 4390937720
# 4390937720. This means that these numbers are pointing to the exact same address
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)  # 11
print("num2 =", num2)  # 22

# 4390937720, same id in memory as before. Integers are immutable in memory
print("\nnum1 points to:", id(num1))
# 4390938072, new and different location in memory
print("num2 points to:", id(num2))


#####################################


dict1 = {
    'value': 11
}

dict2 = dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)  # {'value': 11}
print("dict2 =", dict2)  # {'value': 11}

print("\ndict1 points to:", id(dict1))  # 4378497664
print("dict2 points to:", id(dict2))  # 4378497664. Same address in memory

dict2['value'] = 22

print("\nAfter value is updated:")
# {'value': 22}. Gets updated because dicts are mutable, unlike integers
print("dict1 =", dict1)
print("dict2 =", dict2)  # {'value': 22}

print("\ndict1 points to:", id(dict1))  # 4378497664
# 4378497664. Still the same location in memory as before, both are in the same place
print("dict2 points to:", id(dict2))
