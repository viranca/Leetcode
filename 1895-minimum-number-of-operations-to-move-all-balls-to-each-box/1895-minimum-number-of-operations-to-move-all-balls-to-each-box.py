class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            ans = 0
            for j in range(len(boxes)):
                if j != i:
                    if boxes[j] == "1":
                        ans += abs(i-j)
            answer.append(ans)
        return answer
                    