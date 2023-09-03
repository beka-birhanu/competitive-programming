class Solution:
#         bubble sort
#     def sortColors(self, nums: List[int]) -> None:
#         n = len(nums)
#         i = 0
#         not_sorted = True
#         while i < n and not_sorted:
#             not_sorted = False
#             j = 0
#             while j < n-1:
#                 if nums[j+1] < nums[j]:
#                     nums[j+1], nums[j] = nums[j],nums[j+1]
#                     not_sorted = True
#                 j += 1
#             i += 1


#   selection sort 
#     def sortColors(self, nums: List[int]) -> None:
#         n = len(nums)
#         i = 0
#         while i < n:
#             j = i
#             while j < n:
#                 if nums[i] > nums[j]:
#                     nums[i], nums[j] = nums[j],nums[i]
#                 j += 1
#             i += 1


# selection sort shorter and faster because of the mechanism of for loop
    def sortColors(self, nums: List[int]) -> None:
      for i in range(len(nums)):
          for j in range(i, len(nums)):
              if nums[i] > nums[j]:
                  nums[i], nums[j] = nums[j], nums[i]
