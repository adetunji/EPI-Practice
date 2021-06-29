from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    max_furthest = 0
    last_index = len(A) - 1

    for i in range(0, last_index):
        if i <= max_furthest:
            max_furthest = max(i + A[i], max_furthest)

    return max_furthest >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
