# https://algospot.com/judge/problem/read/TRIANGLEPATH

cache = dict()

def trianglepath(triangle):
	return recur(triangle, 0, 0)

def recur(triangle, y, x):
	global cache
	if y == len(triangle)-1:
		return triangle[y][x]

	if y in cache:
		if x in cache[y]:
			return cache[y][x]
		else:
			cache[y][x] = triangle[y][x] + max(recur(triangle, y+1, x), recur(triangle, y+1, x+1))
	else:
		cache[y] = dict()
		cache[y][x] = triangle[y][x] + max(recur(triangle, y+1, x), recur(triangle, y+1, x+1))
	
	return cache[y][x]

if __name__ == '__main__':
	case = int(input())
	for c in range(case):
		triangle_size = int(input())
		triangle = []
		for i in range(triangle_size):
			row = input()
			triangle.append(list(map(lambda x: int(x), row.split(" "))))
		print(trianglepath(triangle))
		cache = dict()
