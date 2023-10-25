
cnt,length = map(int,input().split())

arr = []

for index in range(int(cnt)):
    arr.append(int(input()))

start = 1
end =  max(arr)

while start <= end:	
    mid = (start + end) // 2
    jull = 0    

    for val in arr:
        jull+= (val // mid)

    if length <= jull:	
        start = mid + 1
    else:			
        end = mid - 1	

print(end)