n, movie = map(int, input().split())
array = list(map(int, input().split()))

start = min(array)
end = sum(array)

result = 0


while start <= end:
    mid = (start + end) // 2

    count = 1
    length = 0

    for i in range(n):
        length += array[i]
        if length > mid:
            count += 1
            length = array[i]

    if count <= movie:
        result = mid
        end = mid - 1

    else:
        start = mid + 1

print(result)



