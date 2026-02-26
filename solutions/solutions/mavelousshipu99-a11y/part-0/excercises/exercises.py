# 01-Beginner Excercise- part 0

## Exercis 1: profile creator
name = "Mavelous"
age = 22
height = 1.7
is_student = True


print(f"name: {name}, type: {type(name)}")
print(f"age: {age}, type: {type(age)}")
print(f"height: {height}, type: {type(height)}")
print(f'is_student: {is_student}, type: {type(is_student)}')


# Exercise 2: Type challenge
a = "10"
b = 10
c = 10.0

print(type(a))
print(type(b))
print(type(c))
# can't add a+b (because we cannot add str + int)
# can add b+c (because we can add int + float = float)