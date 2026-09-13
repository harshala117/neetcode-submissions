class Solution:
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        total = 0
        count = 0
        for n in nums:
            total += n
            r = total % k
            count += seen[r]
            seen[r] += 1
        return count