class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = list(zip(*matrix))
        for row in trans:
            return trans
        