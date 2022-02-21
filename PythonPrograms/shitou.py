count = 3
while count > 0:
    import random
    result = random.randint(97,99)
    print('还有', count ,'把')
    count = count - 1
    guess = input('石头剪刀布:')
    if result == 97:
        print('石头')
    if result == 98:
        print('剪刀')
    if result == 99:
        print('布')
print('游戏结束')