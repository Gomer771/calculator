def add(a, b):
    return a + b 

def multiply(a, b):
    return a * b 

def subtract(a, b):
    return a - b

def squart(a, b):
    return a / b

user_input = input("Введите выражение: ")
result = 0

if "+" in user_input:
    number_list = user_input.split("+")
    result = float(number_list[0])
    for i in range(1, len(number_list)):
        number_list[i] = float(number_list[i])
        result = add(result, number_list[i])


elif "*" in user_input:
    number_list = user_input.split("*")
    result = float(number_list[0])
    for i in range(1, len(number_list)):
        number_list[i] = float(number_list[i])
        result = multiply(result, number_list[i])


elif "-" in user_input:
    number_list = user_input.split("-")
    result = float(number_list[0])
    for i in range(1, len(number_list)):
        number_list[i] = float(number_list[i])
        result = subtract(result, number_list[i])

elif "/" in user_input:
    number_list = user_input.split("/")
    result = float(number_list[0])
    for i in range(1, len(number_list)):
        number_list[i] = float(number_list[i])
        result = squart(result, number_list[i])

print(result)
