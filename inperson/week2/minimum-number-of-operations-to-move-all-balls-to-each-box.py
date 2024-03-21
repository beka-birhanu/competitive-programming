class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)

        pre = 0
        pre_seen = 0
        post = 0
        post_seen= 0
        for i in range(len(boxes)):
            ans[i] += pre_seen*i-pre
            if boxes[i] == "1":
                pre += i
                pre_seen += 1
            ans[len(boxes)-1-i] += post-post_seen*(len(boxes)-1-i)
            if boxes[len(boxes)-1-i] == "1":
                post += len(boxes)-1-i
                post_seen += 1
        return ans

            