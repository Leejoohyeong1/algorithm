#      *      1 5 1     
#     ***     2 4 3 
#    *****    3 3 5
#   *******   4 2 7 
#  *********  5 1 9 
# *********** 6 0 11 

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))


n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)


