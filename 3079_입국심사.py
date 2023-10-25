
cnt,people = map(int,input().split())
# people = 10

# arr = [3,8,3,6,9,2,4]
# arr = [7,10]
arr = []
for index in range(int(cnt)):
    arr.append(int(input()))

start = 1
end =  max(arr) * people

while start <= end:	
    mid = (start + end) // 2
    jull = 0    

    for val in arr:
        jull += (mid // val)

    if people > jull:	
        start = mid + 1
    else:			
        end = mid - 1	


print(f"{start}")



# def solution(n, times):

#         # cnt,people = map(int,input().split())
#     people = n

#         # arr = [3,8,3,6,9,2,4]
#         # arr = [7,10]
#     arr = times
#     # for index in range(int(cnt)):
#     #     arr.append(int(input()))

#     start = 1
#     end =  max(arr) * people

#     while start <= end:	
#         mid = (start + end) // 2
#         jull = 0    

#         for val in arr:
#             jull += (mid // val)

#         if people > jull:	
#             start = mid + 1
#         else:			
#             end = mid - 1	
            
#     return start