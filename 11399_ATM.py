cnt = int(input())
list = list(map(int,input().split()))
list.sort()


total = 0 


for val in range(cnt+1):
    total += sum(list[0:val])

print(total)



