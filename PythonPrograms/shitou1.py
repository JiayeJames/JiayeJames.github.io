import random
dic = {}
dic[0] = '石头'
dic[1] = '剪刀'
dic[2] = '布'
while True:
    humanStr = input('请输入数字[0:石头, 1:剪刀, 2:布]')
    if humanStr.isdigit() and (int(humanStr) in [0,1,2]):
        human = int(humanStr)
        windows = random.randint(0,2)
        print('你出的是', dic[human], '，电脑出的是', dic[windows])
        if (human == 1 and windows == 2) or (human == 2 and windows == 0) or (human == 0 and windows == 1):
            print('你赢了！')
        elif human == windows:
            print("平局")
        else:
            print("你输了")
    else:
        print ("请重新输入!")