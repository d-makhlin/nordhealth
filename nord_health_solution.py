from typing import Dict, List, Set, Tuple

from collections import defaultdict


class NordHealthSolution:

    @staticmethod
    def get_pairs_with_equal_sum_dict(nums: List[int]) -> Dict[int, Set[Tuple[int]]]:
        sum_pairs = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # O(n^2) time complexity
                pair_sum = nums[i] + nums[j]
                sum_pairs[pair_sum].add((min(nums[i], nums[j]), max(nums[i], nums[j])))

        # Filtering only repeated sums
        return {summ: pairs_set for summ, pairs_set in sum_pairs.items() if len(pairs_set) >= 2}

    @staticmethod
    def to_print(sum_pairs_dict: Dict[int, Set[Tuple[int]]]):
        for summ, pairs_set in sum_pairs_dict.items():
            print(f"Pairs : {' '.join(map(str, pairs_set))} have sum : {summ}")
