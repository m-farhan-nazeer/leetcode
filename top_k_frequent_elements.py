from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        sorted_items = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        res = [item[0] for item in sorted_items[:k]]
        return res
