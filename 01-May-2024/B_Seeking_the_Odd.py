for _ in range(int(input())):
    n = int(input())
    while n > 1:
        if n % 2:
            print("YES")
            break
        n //= 2

    else:
        print("NO")
