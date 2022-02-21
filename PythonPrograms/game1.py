import random
secret = random.randint(1,10)
temp = input('Guess a number')
guess = int(temp)
if guess == secret:
    print('Well done!')
else:
    count = 3
    while guess != secret:
        print ('Chance remaining:', count)
        count = count - 1
        if count >= 0:
            temp = input('Try again')
            guess = int(temp)
            if guess == secret:
                print('Well done!')
            else:
                if guess > secret:
                    print('Try a smaller number')
                else:
                    print('Try a bigger number')
        else:
            break
    print ('The answer is', secret)
print('Game Over')