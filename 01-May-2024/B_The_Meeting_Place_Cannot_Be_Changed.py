n = int(input())
f = list(map(int, input().split()))
v = list(map(int, input().split()))
fv = sorted(zip(f, v))
left = fv[0][0]
right = fv[-1][0]

dif = pow(10, -6)
ans = float('inf')
while right - left >= dif:
    mid = (left+right)/2

    left_time = 0
    right_time = 0
    for f, v in fv:
        if f < mid:
            left_time = max(left_time, (mid-f)/v)

        else:
            right_time = max(right_time, (f-mid)/v)

    ans = min(ans, max(left_time, right_time))
    # print(left, right, left_time, right_time)
    if left_time >= right_time:
        right = mid
    else:
        left = mid


print(ans)if ans < float('inf') else print(0)
