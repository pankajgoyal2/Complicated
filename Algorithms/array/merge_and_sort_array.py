import array

arr1 = array.array('b', [2, 9, 11, 17])
arr2 = array.array('b', [1, 5, 6, 13, 20])
print("array1 is : ", arr1)
print("array2 is : ", arr2)
for i in arr2:
    count = 0
    for l in arr1:
        count += 1
        if i < l:
            arr1.insert(count-1, i)
            break



for i in arr2:
    if i not in arr1:
        arr1.append(i)

print("updated array is : ", arr1)
