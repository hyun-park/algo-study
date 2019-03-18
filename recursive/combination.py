out = []
def comb_recur(entry, topick, picked):
	if topick == 0:
		out.append(picked)
		return

	for i in range(len(entry)):
		picked.append(entry[0])
		new_picked = picked.copy()
		comb_recur([j for j in entry if j != entry[0]],     topick-1, new_picked)
		picked.pop()
		entry.pop(0)

	return out
if __name__ == '__main__':
	print(comb_recur([1,3,5,7], 2, []))
