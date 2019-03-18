out = []
def perm_recur(entry, topick, picked):
	global out
	if topick == 0:
		out.append(picked)
		return

	for i in range(len(entry)):
		picked.append(entry[i])
		new_picked = picked.copy()
		perm_recur([j for j in entry if j != entry[i]], topick-1, new_picked)
		picked.pop()

	return out

if __name__ == '__main__':
	print(perm_recur([1,3,5,7], 2, []))
