# https://algospot.com/judge/problem/read/JUMPGAME

cache = dict()

def jumpgame(board):
	if recur(board, 0, 0):
		return "YES"
	else:
	 	return "NO"

def recur(board, y, x):
	global cache

	if y >= len(board.values()) or x >= len(board.values()):
		return False
	if board[y][x] == 0:
	 	return True

	if y in cache:
		if x in cache[y]:
			return cache[y][x]
		else:
			cache[y][x] = recur(board, y + board[y][x], x) or recur(board, y, x + board[y][x])
			return cache[y][x]
	else:
		cache[y] = {}
		cache[y][x] = recur(board, y + board[y][x], x) or recur(board, y, x + board[y][x])
		return cache[y][x]

if __name__ == '__main__':
	case = input()
	for c in range(int(case)):
		size = input()
		board = {}
		for i in range(int(size)):
			row = input()
			board[i] = list(map(lambda x: int(x), row.split(" ")))
		print(jumpgame(board))
		cache = dict()

