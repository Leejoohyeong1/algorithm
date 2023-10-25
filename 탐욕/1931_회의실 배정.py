cnt = int(input())
array = []
for i in range(cnt):
    array.append(list(map(int,input().split())))

array.sort(key=lambda x:(x[1], x[0]))
count = 0
pibot = [0,0]

for val in array:
    if(pibot[1] <= val[0]):
        pibot = val
        count+=1
        
    
print(count)
            
    


