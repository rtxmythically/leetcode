class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        i=0
        while i<len(nums):
            complement=target-nums[i]
            if complement in seen:
                return [i,seen[complement]]
            seen[nums[i]]=i
            i+=1
//解題思路先創一個dict再找dict裡有沒有要的數字
