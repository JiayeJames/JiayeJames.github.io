import random
exit_flag = False
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
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")
        elif human == windows:
            print("平局")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")
        else:
            print("不好意思，你输了")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")
        while True:
            if oncemore == 'y' or oncemore == 'Y':
                break
            elif oncemore == 'n' or oncemore == 'N':
                exit_flag = True
                break #跳出内层循环，并且设置flag
            else:
                oncemore = input("你想再来一局吗? y(Y) or n(N) ")
                if exit_flag == True:
                    break #跳出层循环，结束程序
    else:
        print ("请重新输入!")