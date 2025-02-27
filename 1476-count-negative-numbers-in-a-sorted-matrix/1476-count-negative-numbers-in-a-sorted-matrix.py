class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bs(row):
            left,right = 0,len(row)-1
            while left < right:
                mid = (left+right)//2
                if row[mid] >= 0:
                    left = mid+1
                else:
                    right = mid
            return left

        ans = 0
        for row in grid:
            pivot = bs(row)
            if row[pivot] < 0:
                ans += (len(row)-pivot)
        return ans

                
