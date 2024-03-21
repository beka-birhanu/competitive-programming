class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        finally nums = [zero's,one's,two's]
        where zero's = [:red]
              one's = [red:blue]
              two's = [blue:]
        """
        red,    white,blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] > 1:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            elif nums[white] == 1:
                white += 1
            
            else:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1