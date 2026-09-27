class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}

        prefix = 0
        count = 0

        for n in nums:
            prefix += n

            diff = prefix - k

            if diff in prefixMap:
                count += prefixMap[diff]

            prefixMap[prefix] = prefixMap.get(prefix, 0) + 1
        return count
