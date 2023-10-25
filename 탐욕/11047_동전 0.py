cnt,have_momey = map(int,input().split())

momey = []

for index in range(int(cnt)):
    momey.append(int(input()))

momey.reverse()
cnt = 0
for pay in momey:
    cnt += have_momey // pay
    have_momey = have_momey % pay


print(cnt)

