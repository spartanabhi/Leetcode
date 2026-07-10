class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_col = min_row = 0
        max_col , max_row = len(matrix[0]), len(matrix)
        row = 0
        output = []
        

        while min_col<max_col and min_row<max_row:
            for col in range(min_col,max_col):
                output.append(matrix[row][col])
            min_row +=1

            for row in range(min_row , max_row):
                output.append(matrix[row][col])
            max_col -=1

            if min_col<max_col and min_row<max_row:
                for col in range(max_col-1,min_col-1,-1):
                    output.append(matrix[row][col])
                max_row -=1

                for row in range(max_row-1,min_row-1,-1):
                    output.append(matrix[row][col])
                min_col +=1
        return output
