def selection_sort(data):
    values=data.copy()
    # TODO
    return values

def insertion_sort(data):
    values=data.copy()
    # TODO
    return values

test_cases = [
    [64, 25, 12, 22, 11, 5],
    [1, 2, 3, 4, 5, 7, 6],
    [7, 6, 5, 4, 3, 2, 1],
    [7, 7, 3, 7, 2, 1, 14],
    [],
    [42]
]

for data in test_cases:
    expected = sorted(data)

    selection_result = selection_sort(data)
    insertion_result = insertion_sort(data)

    print("Original:", data)
    print("Expected:", expected)
    print("Selection:", selection_result)
    print("Insertion:", insertion_result)

   
