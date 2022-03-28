def sort(A, n, comp):
	if n == 1:
		return A, comp
	elif n == 0:
		return [], comp
	else:
		comp += n - 1 # tính # phép so sánh ở loại hiện tại, là n - 
		A, p = choosepivot(A, n) # chọn trục
		A, i = partition(A, n) # di chuyển trục đến đúng vị trí i

		# print(f"sort left: {A[ : i - 1]}")
		C, comp = sort(A[: i - 1], i - 1, comp) # sắp xếp đệ quy phần bên trái, tiếp tục theo dõi phần

		# print(f"sort right: {A[i : n]}")
		D, comp = sort(A[i : n], n - i, comp) # sắp xếp đúng phần

		# print(f"C = {C}; D = {D}\n")
		return C + [p] + D, comp 
# nối các danh sách lại với nhau.

def choosepivot(A, n):

## c1: Luôn chọn mục đầu tiên làm trục:
# p = A [0]

## c2: Luôn chọn mục cuối cùng làm trục:
# p = A [n - 1]
# A [0], A [n - 1] = A [n - 1], A [0]

## c3: Chọn trung bình của ba mục (đầu tiên, giữa, cuối cùng) làm trục
	Medianlst = [A[0], A[n - 1], A[(n + 1) // 2 - 1]]
	p = sorted(Medianlst)[1]
	if p == A[n - 1]:
		A[0], A[n - 1] = A[n - 1], A[0]
	elif p == A[(n + 1) // 2 - 1]:
		A[0], A[(n + 1) // 2 - 1] = A[(n + 1) // 2 - 1], A[0]

	return A, p

def partition(A, n):
	p = A[0]
	i = 1
	for j in range(0, n):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i += 1
	A[0], A[i - 1] = A[i - 1], A[0]
	# print(f"A = {A}; p = {p}; i = {i}")
	return A, i

#----------------------------------------------------------


unsorted = []

with open('D:\QuickSort.txt') as file:
   for line in file:
       unsorted.append(int(line))

comp = 0
sorted, comp = sort(unsorted, len(unsorted), comp)
print(sorted, f"comparisons = {comp}")