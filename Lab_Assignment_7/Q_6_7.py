def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code

def selectionSort (arr, size):
    for step in range(size):
        minimum = step
        for i in range(step + 1 , size):
            if arr[i] < arr[minimum]:
                minimum = i
# Swap
        (arr[step], arr[minimum]) = (arr[minimum], arr[step])
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
x=Remove(duplicate)
size = len(x)
selectionSort(x, size)
print( 'Sorted Array in Ascending Order: ' )
print(x)