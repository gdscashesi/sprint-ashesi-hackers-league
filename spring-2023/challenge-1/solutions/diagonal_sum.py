from typing import List


def diagonalSum(matrix: List[List[int]]) -> int:
    """
    pd_ptr : primary diagonal pointer -> tracks the index of the primary diagonal
    sd_ptr : secondary diagonal pointer -> tracks the index of the secondary diagonal

    Time Complexity: O(n), where n is the number of rows in the matrix
    Space Complexity: O(1)
    """
    # initializing pointers
    pd_ptr, sd_ptr = 0, len(matrix[0]) - 1

    # diagonal sum, initially zero
    diagonal_sum = 0

    for row in matrix:
        # sum the values at both pointers
        # if the pointers point to different indices
        diagonal_sum += row[pd_ptr] + (row[sd_ptr] if pd_ptr != sd_ptr else 0)

        # move the pointers
        pd_ptr += 1
        sd_ptr -= 1

    return diagonal_sum
