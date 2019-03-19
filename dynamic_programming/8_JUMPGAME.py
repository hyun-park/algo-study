import numpy as np

def jumpgameSolve(board):
	state_board = np.full((len(board), len(board[0])), -1)
	np_board = np.array(board)

	return recur(state_board, np_board, 0,0)

def recur(state_board, np_board, y, x):
	if y >= len(np_board) or x >= len(np_board):
		return 0
	if np_board[y,x] == "0":
		return 1
	if state_board[y,x] != -1:
	 	return int(state_board[y,x])
	jump_size = int(np_board[y,x])
	state_board[y,x] = recur(state_board, np_board, y + jump_size, x) or recur(state_board, np_board, y, x + jump_size)
	return int(state_board[y,x])


if __name__ == '__main__':
	size = input()
	board = []
	for i in range(int(size)):
		row = input()
		board.append(row.split(" "))
	print(jumpgameSolve(board))

