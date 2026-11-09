class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Set up the number of rows and columns
        rows, columns = len(matrix), len(matrix[0])

        # Get to the end of the 2d array using rows * columns - 1
        l, r = 0, rows * columns - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # m // columns counts how many complete rows there are before index m
            # m % columns gives the leftover positions within the current row
            row, column = m // columns, m % columns

            if target > matrix[row][column]:
                l = m + 1
            elif target < matrix[row][column]:
                r = m - 1
            else:
                return True

        return False