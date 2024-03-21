class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        d = defaultdict(int) # this to store two candidates. it will have maximum of 2 lenght

        # look for at most two candidates
        for num in nums:
            d[num] += 1

            if len(d) > 2:
                # remove the candidate whose count is zero
                # create another dict since we cant change the size of the original during iteration
                new_d = defaultdict(int)
                for key,val in d.items():
                    if val > 1:
                        new_d[key] = val-1
                d = new_d


        """ check if the candidates are realy majority element
        
        *first reset their counts to zero
        *then count their apperance as they appear
        *finally compare their count to n//3 to check if they are realy majority numbers
        """
        
        for key,val in d.items():
                d[key] = 0


        for num in nums:
            if num in d:
                d[num] += 1
        return list(key for key,val in d.items() if val > len(nums)//3) 