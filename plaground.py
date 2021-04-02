

def bubble_sort_enum(array):
    swapped = True
    while swapped:
        swapped = False
        for index, item in enumerate(array[:-1]):
            if item > array[index+1]:
                array[index] = array[index+1]
                array[index+1] = item
                swapped = True
    return array


alphabet = ["c", "d", "a", "b"]
numbers = [4, 3, 2, 1]

def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        print(f"\nLooping through the array {array}")
        for index in range(0, len(array)-1, 1):
            if array[index] > array[index+1]:
                print(f"{array[index]} at index {index} < {array[index+1]} at index {index+1} so they are swapped")
                print(array)
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
                swapped = True
    return array


def insertion_sort(array):
    sorted_array = [array[0]]
    for item in array[1:]:
        for i in range(len(sorted_array)):
            if item < sorted_array[i]:
                sorted_array.insert(i, item)
                break
        else:
            sorted_array.append(item)
    return sorted_array




scene = "01opening"
scene_number = scene[0:2]
print(scene_number)