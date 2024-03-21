class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        for key,val in count_t.items():
            if key not in count_s:
                return ""
            elif val > count_s[key]:
                return ""

        missing = len(t)
        queue = collections.deque()

        left = 0
        min_window = [0,len(s)+1]

        for right,char in enumerate(s):

            if char in count_t:
                queue.append(right)
 
                if count_t[char] > 0:
                    missing -= 1

                count_t[char] -= 1

                while not missing:
                    left = queue.popleft()
                    char = s[left]

                    count_t[char] += 1
                    if count_t[char] > 0:
                        missing += 1

                        if right - left < min_window[1]-min_window[0]:
                            min_window = [left,right+1]

                        break

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]]

