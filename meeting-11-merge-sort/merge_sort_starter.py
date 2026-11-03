
def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(data):

    # Base case
    if len(data) <= 1:
        return data.copy()

    # Divide
    middle = len(data) // 2

    left = data[:middle]
    right = data[middle:]

    # Conquer
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Combine
    return merge(left_sorted, right_sorted)


numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original:", numbers)
print("Sorted:", merge_sort(numbers))



