# https://algospot.com/judge/problem/read/LIS
# 틀리다고 나옴

cache = dict()
def lis(seq):
	return recur(seq, 0)

def recur(seq, start):
	if len(seq) == 0:
		return 0

	if start in cache:
		return cache[start]
	else:
		max_len = 0
		for i in range(len(seq)):
			sub_seq = list(filter(lambda x: x > seq[i],seq[i+1:len(seq)]))
			max_len = max(max_len, 1+ recur(sub_seq, i+start))
			cache[start+i] = max_len
		
		return max_len

if __name__ == '__main__':
	case = int(input())
	for c in range(case):
		seq_length = int(input())
		seq = list(map(lambda x: int(x), input().split(" ")))
		print(lis(seq))
