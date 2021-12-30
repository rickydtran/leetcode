class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 2D Array to store rows
        res = [[] for i in range(numRows)]
        row = 0
        delta = -1
        
        # Iterate through each character in string and
        # append to given row based off number of rows
        for c in s:
            res[row].append(c)
            # Toggle delta when we reach either 0 or num_rows
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
        
        # Convert each array in res to string and concatenate to
        # for our final string
        for i in range(len(res)):
            # print(res[i])
            res[i] = ''.join(res[i])
        return ''.join(res)