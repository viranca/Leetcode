class Solution:
    def isHappy(self, n: int) -> bool:

        def happy_iterate(n):
            new = 0
            for i in str(n):
                new += int(i)**2
            return new

        hash_set = set()
        iterate = n
        while iterate not in hash_set:
            hash_set.add(iterate)
            iterate = happy_iterate(iterate)
            
            if iterate == 1:
                return True
        return False