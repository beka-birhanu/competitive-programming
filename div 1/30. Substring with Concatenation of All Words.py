# Runtime 78ms and Memory 16.82MB

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        word_cnt = Counter(words)

        for index in range(len(words[0])):
            i = j = index
            count = 0
            current_sub = defaultdict(int)
            
            while j + len(words[0]) <= len(s):
                substr = s[j:j + len(words[0])]
                j += len(words[0])
                
                if substr not in word_cnt:
                    current_sub.clear()
                    count = 0
                    i = j
                else:
                    current_sub[substr] += 1
                    count += 1

                    while current_sub[substr] > word_cnt[substr]:
                        current_sub[s[i:i + len(words[0])]] -= 1
                        i += len(words[0])
                        count -= 1
                    
                    if count == len(words):
                        ans.append(i)
        
        return ans
