comparison_count = 0
def quicksort_pivot_end(array):
    '''array is a list of integers
    returns the same list sorted from smallest to largest'''
    global comparison_count
    
    # Trường hợp cơ sở, mảng đã được sắp xếp
    if len(array) <= 1:
        return array
    # Trong phiên bản đơn giản, pivot luôn là phần tử đầu tiên của mảng
    pivot = array[len(array)-1]
    # swap pivot lấy đầu tiên trong mảng
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
    # phân vùng mảng đầu vào xung quanh trục bằng cách sử dụng triển khai tại chỗ
    # để việc sử dụng bộ nhớ được tối thiểu hóa
    i = 1  # ranh giới trong các phần tử đã thấy giữa <pivot và> pivot
    j = 1  # ranh giới giữa các phần tử đã xem và các phần tử chưa được nhìn thấy
    for index in range(1, len(array)):

        if array[index] < pivot:
            j += 1
            array[index], array[i] = array[i], array[index]
            i += 1
        else:
            j += 1
            
    comparison_count += (len(array)-1)

    # hoán đổi phần tử pivot vào đúng vị trí của nó
    array[0], array[i-1] = array[i-1], array[0]

    # sắp xếp đệ quy phần đầu tiên
     # sắp xếp đệ quy phần thứ hai
    return quicksort_pivot_end(array[0:i-1]) + [pivot] + quicksort_pivot_end(array[i:])



my_test = [4, 6, 2, 8, 45, 1, 98, 100, 3, 23]

final = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]

Quicksort_file = open('D:\QuickSort.txt', 'r')
final = []

for line in Quicksort_file.readlines()[0:10000]:
    num = int(line.strip())
    final.append(num)
quicksort_pivot_end(final)

print("comparisons", comparison_count)

print("final", final)
print("result_array", quicksort_pivot_end(final))