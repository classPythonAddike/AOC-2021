from typing import List


class BingoBoard():
    def __init__(self, board: List[List[int]]):
        self.board = [
            [[num, False] for num in row]
            for row in board
        ]
    
    def mark_number(self, number: int):
        for row_num, row in enumerate(self.board):
            for pos, num in enumerate(row):
                if num[0] == number:
                    self.board[row_num][pos][1] = True

    def has_won(self) -> bool:
        # Check rows
        if any([all([num[1] for num in row]) for row in self.board]):
            return True
        else:
            # Check columns - first invert the board, then apply same logic for checking rows
            inverted_board = list(map(list, zip(*self.board)))
            return any([all([num[1] for num in row]) for row in inverted_board])

    def unmarked_numbers(self) -> List[int]:
        nums = []
        for row in self.board:
            for num in row:
                if not num[1]:
                    nums.append(num[0])
        return nums


with open(0) as f:
    inp = f.read().strip().split("\n")


numbers = map(int, inp[0].strip().split(","))

boards = [
    list(map(
        lambda row: [*map(int, row.split())],
        inp[row_num:row_num + 5]
    ))
    for row_num in range(2, len(inp), 6)
]

boards = [BingoBoard(board) for board in boards]

for num in numbers:
    for board in boards:
        board.mark_number(num)
        if board.has_won():
            print(sum(board.unmarked_numbers()) * num)
            exit()
