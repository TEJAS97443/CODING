a, b = map(int, input().split())
lis = list(map(int, input().split()))
from math import ceil, log2
n = 2 ** ceil(log2(a))
seg = [[10 ** 6, -10 ** 6]] * (2 * n)
for j in range(0, len(lis)):
	seg[j + n] = [lis[j], lis[j]]
for j in range(n - 1, 0, -1):
	seg[j] = [min(seg[2 * j][0], seg[2 * j + 1][0]), max(seg[2 * j][1], seg[2 * j + 1][1])]
def up(ind, val):
	ind += n
	seg[ind] = [val, val]
	ind >>= 1
	while ind > 0:
		seg[ind] = [min(seg[2 * ind][0], seg[2 * ind + 1][0]), max(seg[2 * ind][1], seg[2 * ind + 1][1])]
		ind >>= 1
def r(ind, k):
	ind = ind + n
	flag = True
	while flag and ind <= len(seg) and ind >= 1:
		if ind==1:
			if seg[2*ind + 1][0] < k:
				return -1
			else:
				ind=2*ind + 1
				continue
		if ind >= n and seg[ind][0] >= k:
			return ind - n
		elif ind >= n:
			if ind & 1:
				ind += 1
			ind >>= 1
		else:
			if seg[2*ind][1]>=k:
				ind=2*ind
			elif seg[ind][1] < k:
				ind >>= 1
			else:
				ind = ind * 2 + 1
	return -1
if len(lis) == 1:
	for j in range(0, b):
		tot = list(map(int, input().split()))
		if tot[0] == 2:
			if lis[0] < tot[2]:
				print(-1)
			else:
				print(0)
		else:
			lis[0] = tot[2]
else:
	for j in range(0, b):
		tot = list(map(int, input().split()))
		if tot[0] == 2:
			vayu = r(tot[2], tot[1])
			if vayu == len(lis):
				print(-1)
			else:
				print(vayu)
		else:
			up(tot[1], tot[2])