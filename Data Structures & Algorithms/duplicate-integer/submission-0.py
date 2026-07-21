from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        for count in nums_counter.values():
            if count > 1:
                return True
        return False    