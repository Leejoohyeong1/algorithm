# """
# 5
# *        * * 2  ' ' 8
# **      ** * 4  ' ' 6
# ***    *** * 6  ' ' 4
# ****  **** * 8  ' ' 2
# ********** * 10 ' ' 2
# ****  **** * 8  ' ' 2
# ***    *** * 6  ' ' 4
# **      ** * 4  ' ' 6
# *        * * 2  ' ' 8

def draw_pattern2(n):
    N=int(input())

    for i in range(1,N+1):
        print("*"*i+" "*(N-i)*2+"*"*i)

    for i in range(1,N+1):
        print("*"*(N-i)+(" "*i)*2+"*"*(N-i))

    
def draw_pattern(n):
    for i in range(1, n + 1):
        stars = '*' * i
        spaces = ' ' * (2 * n - 2 * i)
        line = stars + spaces + stars
        print(line)

    for i in range(n - 1, 0, -1):
        stars = '*' * i
        spaces = ' ' * (2 * n - 2 * i)
        line = stars + spaces + stars
        print(line)

pattern_size = int(input())
draw_pattern(pattern_size)

