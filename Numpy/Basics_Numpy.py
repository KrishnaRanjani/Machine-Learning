import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


import numpy as np
one = np.ones(3)
print(one)


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
x=arr.mean()
print(x)


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x=arr.mean()
print(x)



import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
