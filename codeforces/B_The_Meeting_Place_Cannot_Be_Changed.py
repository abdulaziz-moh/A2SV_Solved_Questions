n = int(input())
x = list(map(int,input().split()))
v = list(map(int,input().split()))

def find_dis_long_time(mid):

    mx, val = float("-inf"), x[0]
    for i in range(len(x)):
        time = abs(mid - x[i]) / v[i]
        if time > mx:
            mx = time
            val = x[i]
    return (mx, val)


start, end = min(x), max(x)
time = 0

while end - start >= 0.000001:
    mid = start + (end-start)/2
    time, val = find_dis_long_time(mid)
    if val >= mid:
        start = mid
    else:
        end = mid
print(time)