for _ in range(int(input())):
    s = input()
    if len(s) % 2:
        print("NO")
        continue

    if s[:len(s)//2] == s[len(s)//2:]:
        print("YES")

    else:
        print("NO")
