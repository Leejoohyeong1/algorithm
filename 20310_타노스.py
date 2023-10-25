
str = input()

zreoCnt= str.count("0") // 2
oneCnt= str.count("1") // 2


strList = list(str)


for index in range(len(strList)):
    if(strList[index] == '1'):
        strList[index] = ''
        oneCnt+=-1
        if(oneCnt <= 0):
            break
        


for index in range(len(strList)-1, -1, -1):
    if(strList[index] == '0'):
        strList[index] = ''
        zreoCnt+=-1
        if(zreoCnt <= 0):
            break


print("".join(strList))