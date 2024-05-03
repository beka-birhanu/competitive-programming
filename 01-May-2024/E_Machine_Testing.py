import math


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    st = [(p[0], float('inf'))]
    max_t = 0

    for i in range(1, n):
        curr_h = h[i]
        curr_p = p[i]
        curr_t = 0
        # print(st)
        while curr_h > 0 and math.ceil(curr_h/st[-1][0])+curr_t > st[-1][1]:
            prev_h, prev_t = st.pop()
            curr_h -= prev_h * (prev_t-curr_t)
            curr_t = prev_t

            while st[-1][1] <= curr_t:
                st.pop()

            # print(curr_h, curr_t, st, prev_h, prev_t)
        curr_t += math.ceil(curr_h/st[-1][0])
        st.append((curr_p, curr_t))
        max_t = max(max_t, curr_t)

    # print(st)
    print(max_t)
