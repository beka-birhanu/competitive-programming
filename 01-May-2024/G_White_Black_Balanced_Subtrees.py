
import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    def dfs(curr):
        if color[curr] == "W":
            curr_val = [1, 0, 0]

        else:
            curr_val = [0, 1, 0]

        for child in children[curr]:
            child_val = dfs(child)
            for i in range(3):
                curr_val[i] += child_val[i]

        if curr_val[0] == curr_val[1]:
            curr_val[2] += 1

        return curr_val

    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        color = input()

        children = [[] for i in range(n)]
        for j in range(n-1):
            children[a[j]-1].append(j+1)
        print(dfs(0)[-1])


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
