# 01-Biginner exercisse - part 0

## Exercise 1: profile creator
name = "Mavelous"
age = 22
height = 1.7
is_student = True

print(f"Name: {name}, type: {type(name)}")
print(f"Age: {age}, type: {type(age)}")
print(f"Height: {height}, type: {type(height)}")



#Exercise 2: Type Challenge
a = "10"
b = 10
c = 10.0

print(type(a))
print(type(b))
print(type(c))
# can't add a + b (because we cannot add str + int)
# can add b + c (because we can add int + float = float)

## Exercise 3: Conversion
age_str = input("enter your age: ")
age = int(age_str)
future_age = age + 10
print(f"in 10 years, your will be {future_age}")

# Exercise 4: Text Processing
text =  "hello, world! HELLO"

text = text.strip()
print(text)

text = text.lower()
print(text)

count = text.count("hello")
print(count)

text = text.replace("world", "python")
print(text)


