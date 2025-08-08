import numpy as np
# print(np.__version__)


# List1D=[1,2,3,4,5,6,7,8,9,10]
# List2D=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30]]

list1D = [1, 2, 3, 4, 5]
list2D = [[1, 2, 3], [4, 5, 6]]
array1D = np.array(list1D)
array2D = np.array(list2D)
print("1D Array :", array1D , list1D)
print("Shape:", array1D.shape)

print("2D Array :", array2D)
print("2D List :", list2D)
print("Shape:", array2D.shape)