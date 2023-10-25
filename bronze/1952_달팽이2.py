# 5 3

def move(cursor, direction):
    move = [0,0]
    move[0] = cursor[0] + direction[0]
    move[1] = cursor[1] + direction[1]
    return move

def mapOverCheck(map, moveCheck):

    return False


# rows, cols = list(map(int,input().split()))
rows = 5
cols = 3
map = [[0] * cols] * rows
cursor =  [0,0]

left = [0,1]
down = [-1,0]
right = [0,-1]
up = [1,0]


direction = left
directioncheck = [0,0]

directioncheck = move(cursor,direction)

print(directioncheck) 




# print(map)

