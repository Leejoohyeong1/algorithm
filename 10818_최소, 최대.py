"""
5
20 10 35 30 7

7 35
"""
cnt = input()
array = list(map(int,input().split()))

minVal = min(array)
maxVal = max(array)

print(f"{minVal} {maxVal}")