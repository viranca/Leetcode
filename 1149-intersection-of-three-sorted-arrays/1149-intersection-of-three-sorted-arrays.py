class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []
        arrset2 = set(arr2)
        arrset3 = set(arr3)
        for number in arr1:
            if number in arrset2 and number in arrset3:
                ans.append(number)
        return ans
