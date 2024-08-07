# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        typed_count = 0
        key_press_count = 0
        for _, count in count.most_common():
            typed_count += 1
            key_press_count += math.ceil(typed_count/8)*count
        
        return key_press_count