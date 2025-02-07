class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        while len(matrix)>1:
            out.extend(matrix[0])
            for i in range(len(matrix)-2):
                i+=1
                if matrix[i]:
                    out.append(matrix[i][-1])
                    matrix[i].pop()
        
            out.extend(matrix[-1][::-1])

            for i in reversed(range(len(matrix)-2)):
                i+=1
                if matrix[i]:
                    out.append(matrix[i][0])
                    matrix[i].pop(0)

            matrix.pop(0)
            matrix.pop()
        if matrix:
            out.extend(matrix[0])

        return(out)
            
