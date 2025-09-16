# 1 задача
import numpy as np

X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])

a = np.diag(X)
a = a[a!=0]
k = np.prod(a)
print(k)

# 2 задача
import numpy as np

x = np.array([1, 2, 2, 4])
y = np.array([4, 2, 1, 2])
x.sort()
y.sort()
print(np.array_equal(x, y))

# 3 задача
import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
mask = (x == 0)
mask = mask[:-1]
print(x[1:][mask].max())

# 4 задача

# 5 задача

import numpy as np
x = np.array([2, 2, 2, 3, 3, 3, 5])
x1, x2 = np.unique(x, return_counts=True)
print((x1, x2))

# 6 задача


