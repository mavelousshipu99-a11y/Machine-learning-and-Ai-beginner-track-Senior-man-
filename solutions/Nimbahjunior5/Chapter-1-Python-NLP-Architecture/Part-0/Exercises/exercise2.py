a = "10"
b = 10
c = 10.0

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>

# Can't add a + b (str + int)
# Can add b + c (int + float = float)
result = b + c  # 20.0