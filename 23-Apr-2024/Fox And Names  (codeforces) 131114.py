# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
N = int(input())
alien_dict = [input() for _ in range(N)]
order_graph = defaultdict(set)
before_count = defaultdict(set)
letters = 'qwertyuiopasdfghjklzxcvbnm'

for i in range(N-1):
    word1 = alien_dict[i]
    word2 = alien_dict[i+1]
    
    for k in range(min(len(word1), len(word2))):
        if word1[k]!=word2[k]:
            order_graph[word1[k]].add(word2[k])
            before_count[word2[k]].add(word1[k])
            break
    else:
        if len(word1) > len(word2):
            print("Impossible")
            exit()

dq = deque()
for letter in letters:
    if len(before_count[letter]) == 0:
        dq.append(letter)

ans = []
while dq:
    curr = dq.popleft()
    ans.append(curr)
    
    for next_letter in order_graph[curr]:
        before_count[next_letter].remove(curr)
        if len(before_count[next_letter]) == 0:
            dq.append(next_letter)

print("".join(ans)) if len(ans) == 26 else print("Impossible")