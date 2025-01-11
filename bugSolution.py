def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return "Error: Cannot divide by zero when both inputs are 0"
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0, 0)
print(result) # Output: Error: Cannot divide by zero when both inputs are 0
result2 = function_with_uncommon_error(5,0)
print(result2) #Output: 5
result3 = function_with_uncommon_error(5,2)
print(result3) #Output: 2.5