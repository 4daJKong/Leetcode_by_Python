from typing import List


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = [list(i) for i in zip(*matrix[::-1])]
        #matrix[::] = zip(*matrix[::-1]) return tuple
        return matrix

            

           


print(Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])) 
print(Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) 
print(Solution().rotate(matrix = [[1,2],[3,4]])) 
print(Solution().rotate(matrix = [[1]])) 