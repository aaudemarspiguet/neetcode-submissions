class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input size always 9 x 9, so time complexity is O(1)

        # check rows for uniqueness
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False # duplicate found
                row_set.add(board[i][j])

        # check cols for uniqueness
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col_set:
                    return False 
                col_set.add((board[i][j]))
        
        # pair a set for each reduced coordinate (key: (red_i, red_j), val: set())
        grid_dict = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                new_coord = tuple([i // 3, j // 3])
                if new_coord not in grid_dict:
                    grid_dict[new_coord] = set()
                if board[i][j] in grid_dict[new_coord]:
                    return False
                grid_dict[new_coord].add(board[i][j])
                
        return True