def triangle():
    line = [1]         # 第一行就一个元素1
    while True:
        yield line
        # 生成下一行，表达式为 : [1] + 上一行的两个元素之和 + [1]
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]



n = 0     # 控制输出行数
for item in triangle():
    print(item)
    n += 1
    if n % 10 == 0:
        break





def triangles():
    N=[1] 　　#初始化为[1],杨辉三角的每一行为一个list
    while True:
        yield N　　#yield 实现记录功能，没有下一个next将跳出循环，
        S=N[:]　　 #将list N赋给S，通过S计算每一行
        S.append(0) #将list添加0，作为最后一个元素，长度增加1
        N=[S[i-1]+S[i] for i in range(len(S))]　　#通过S来计算得出N


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break