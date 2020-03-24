class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                    x = {}
                            for i, v in enumerate(nums):
                                            y = target - v
                                                        if y in x:
                                                                            return [x[y], i]
                                                                                    x[v] = i
