import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
inf = float('inf')

MAX = 2 * 10 ** 5 + 1
# --- BEGIN SPARSE TABLE ---


def precalc_log():
	global LOG
	LOG = [0] * MAX
	for ii in range(2, MAX):
		LOG[ii] = LOG[ii // 2] + 1


def precalc_sparse_table(A):
    global ST
    n = len(A)
    size = LOG[n]
    ST = [[0 for jj in range(n + 1 - (1 << ii))] for ii in range(size + 1)]
    for ii in range(size + 1):
        if ii == 0:
            for jj in range(n):
                ST[ii][jj] = A[jj]
        else:
            for jj in range(0, n + 1 - (1 << ii)):
                ST[ii][jj] = max(ST[ii - 1][jj], ST[ii - 1][jj + (1 << ii - 1)])

def query(l, r):
	log_range = LOG[r - l + 1]
	return max(ST[log_range][l], ST[log_range][r - (1 << log_range) + 1])
# --- END SPARSE TABLE ---


def solution():
    precalc_log()
    row, col = map(int, input().split())
    ht = list(map(int, input().split()))
    precalc_sparse_table(ht)
    for _ in range(int(input())):
        q = list(map(int, input().split()))
        if (q[0] - q[2]) % q[4] == 0 and (q[1] - q[3]) % q[4] == 0:
            if q[0] < ht[q[1]-1] or q[2] < ht[q[3]-1]:
                print("NO")
            else:
                maxHeight = row - (abs(row % q[4] - (q[0] % q[4])))
                start = min((q[1]-1), (q[3]-1))
                end = max((q[1]-1), (q[3]-1))
                if start == end:
                    print("YES")
                elif maxHeight <= query(start, end):
                    print("NO")
                else:
                    print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solution()
