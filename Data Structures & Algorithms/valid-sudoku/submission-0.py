class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[row][col]
                if value==".":
                    continue
                elif value in seen:
                    return False
                else:
                    seen.add(value)
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[col][row]
                if value==".":
                    continue
                elif value in seen:
                    return False
                else:
                    seen.add(value)
        for square_x in range(0,7,3):
            for square_y in range(0,7,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[square_x+i][square_y+j]
                        if value==".":
                            continue
                        elif value in seen:
                            return False
                        else:
                            seen.add(value)
        return True
