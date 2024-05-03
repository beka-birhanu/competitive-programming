from collections import Counter


n, k = map(int, input().split())
s = input()

max_len = 0
freq = {"a": 0, "b": 0}

i = 0
for j, ch in enumerate(s):
    freq[ch] += 1
    while min(freq.values()) > k:
        freq[s[i]] -= 1
        i += 1
    max_len = max(max_len, j-i+1)

print(max_len)
