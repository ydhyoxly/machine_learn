# 1 задача
import numpy as np

X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])

a = np.diag(X)
a = a[a != 0]
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

import numpy as np
from scipy.spatial import distance
import time


X = np.random.rand(25, 3)
Y = np.random.rand(50, 3)



def vector_evc_dist(X, Y):
   
    X_2 = np.sum(X ** 2, axis=1, keepdims=True)
    Y_2 = np.sum(Y ** 2, axis=1)
    XY = np.dot(X, Y.T)
    return np.sqrt(X_2 - 2 * XY + Y_2)



print('Сравнение co scipy:')


start = time.time()
result = vector_evc_dist(X, Y)
end = time.time() - start


scipy_start = time.time()
scipy_result = distance.cdist(X, Y, 'euclidean')
scipy_end = time.time() - scipy_start


print('Векторная реализация: ' + str(end) + ' секунд')
print('Scipy cdist: ' + str(scipy_end) + ' секунд')
dif = end/scipy_end

print('Scipy быстрее векторной реализации в ' + str(dif) + 'раз')
print(result)
print(scipy_result)

# 5 задача

import numpy as np
x = np.array([2, 2, 2, 3, 3, 3, 5])
x1, x2 = np.unique(x, return_counts=True)
print((x1, x2))

# 6 задача

import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("изображение")

img_arr = np.asarray(img)
img_arr_1 = img_arr.tolist()



def vector_summ(image, weights):
    
    return np.tensordot(image, weights, axes=([2], [0]))


gray_weights = np.array([0.299, 0.587, 0.114])

plt.figure(figsize = (15, 10))


plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Изначальное изображение')
plt.axis('off')


plt.subplot(1, 3, 3)
gray_img_2 = vector_summ(img_arr, gray_weights)
plt.imshow(gray_img_2, cmap='gray')
plt.title('Серое векторизованное изображение')
plt.axis('off')






