alph = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):

    n, k = map(int, input().split())
    min_freq = n // k
    rem = n % k
    print(alph[:k]*min_freq + "a"*rem)
