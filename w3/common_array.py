import numpy as np
arr1=[[1,5,2,4,7,8],[2,1,8,3,6,4]]
arr2=[[2,1,8,3,7,4],[1,5,2,4,8,5]]
common=np.intersect1d(arr1,arr2)
print(common)
