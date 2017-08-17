def shuixianhua():
    for i in range(100,1000):
        temp = i
        sum = 0
        while temp:
            sum =sum + (temp%10) ** 3
            temp = temp // 10

        if sum == i:
            print(i,end=' ')

print('所有水仙花数为：',end=' ')

shuixianhua()
            


 
