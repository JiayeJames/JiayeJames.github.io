def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

number = int(input('几的阶乘：'))
result = factorial(number)
print('%d的阶乘是%d' % (number, result))