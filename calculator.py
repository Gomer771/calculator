def add(a, b):
    return a+b 

def multiply(a, b):
  return a*b 

def subtract(a, b):
        return a-b


user_input=input("Введите выражение")
result = 0
if "+" in user_input:
    user_input=user_input.split("+")
    for i in range(0, len(user_input)):
        user_input[i]= float (user_input[i])
        result=(result, user_input[i])
else:

    result = 1
if "*" in user_input:
    user_input=user_input.split("*")
    for i in range(0, len(user_input)):
        user_input[i]= float (user_input[i])
        result=multiply(result, user_input[i])
else:

    result = 0
if "-" in user_input:
    user_input=user_input.split("-")
    for i in range(0, len(user_input)):
        user_input[i]= float (user_input[i])
        result=subtract(user_input[i], result)

print(result)
