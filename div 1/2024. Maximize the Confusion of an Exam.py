Runtime 271 ms and Memory 16.6 MB
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_cnt = 0
        f_cnt = 0
        i = 0
        ans = 0
        for j in range(len(answerKey)):
            if answerKey[j] == "F":
                f_cnt += 1
            else:
                t_cnt += 1
            while min(f_cnt, t_cnt) > k:
                if answerKey[i] == "F":
                    f_cnt -= 1
                else:
                    t_cnt -= 1
                i += 1
            ans = max(ans,j-i+1)
        return ans

Runtime301 ms and Memory 18.7 MB
class Solution_2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        f = deque()
        ans = 0
        i = 0
        for j in range(len(answerKey)):
            if answerKey[j] == "F":
                f.append(j)
                if len(f) > k:
                    i = f.popleft() + 1
            ans = max(ans, j-i+1)

        t = deque()
        i = 0    
        for j in range(len(answerKey)):
            if answerKey[j] == "T":
                t.append(j)
                if len(t) > k:
                    i = t.popleft() + 1
            ans = max(ans, j-i+1)
        return ans
