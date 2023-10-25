

cnt,length =  list(map(int,input().split()))

arr =  list(map(int,input().split()))

# length = 7
# arr = [20, 15, 10, 17]
# length = 20
# arr = [4, 42, 40, 26, 46]
# length = 2
# arr= [100,100]



start = 1
end =  max(arr)

while start <= end:	
    mid = (start + end) // 2
    jull = 0    


    for val in arr:
        if(val > mid):
            jull += (val-mid)
    
    if length <= jull:	
        start = mid + 1
    else:			
        end = mid - 1	

print(end)

