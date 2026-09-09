class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        for num, ct in counts.items():
            freq[ct].append(num)

        result = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                result.append(num)
                if len(result) == k:
                    return result
                