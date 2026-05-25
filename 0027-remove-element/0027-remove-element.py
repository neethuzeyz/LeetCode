class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        low  = 0                  # Next position to check from the left
        high = len(nums) - 1      # Next position to check from the right

        while low <= high:

            if nums[low] != val:
                low += 1          # Already valid → keep and advance

            elif nums[high] == val:
                high -= 1         # Both ends are val → discard right side

            else:
                # nums[low]==val and nums[high]!=val → swap to fix both at once
                nums[low], nums[high] = nums[high], nums[low]
                low  += 1
                high -= 1

        return low                # [0..low-1] contains exactly k valid elements