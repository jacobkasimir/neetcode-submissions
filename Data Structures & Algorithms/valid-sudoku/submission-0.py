class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        colls = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for k in range(9):
                val = board[i][k]
                if (val == "." ):
                    continue
                else:
                    if val in rows[i]:
                        return False
                    elif val in colls[k]:
                        return False
                    elif val in boxes[(i//3, k //3)]:
                        return False
                    else:
                        rows[i].add(val)
                        colls[k].add(val)
                        boxes[(i//3, k//3)].add(val)
        return True