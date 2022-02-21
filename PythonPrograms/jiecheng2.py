def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('几的阶乘：'))
result = factorial(number)
print('%d的阶乘是%d' % (number, result))