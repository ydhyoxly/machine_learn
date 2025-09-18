# 1 задача
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([200, 500, 1000, 2300, 3000, 5890, 7560, 10000])
time_non_vectorized = np.array([70, 130, 330, 980, 1420, 2560, 3300, 6450])
time_vectorized = np.array([60, 38, 67, 101, 130, 670, 870, 1100])
ax2 = fig.add_subplot(111)


ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"1 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()

# 2 задача

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([200, 500, 1000, 2300, 3000, 5890, 7560, 10000])
time_non_vectorized = np.array([40, 110, 200, 600, 800, 1550, 2200, 3100])
time_vectorized = np.array([400, 300, 230, 250, 300, 450, 500, 660])
ax2 = fig.add_subplot(111)


ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"2 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()


# 3 задача

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([200, 500, 1000, 2300, 3000, 5890, 7560, 10000])
time_non_vectorized = np.array([80, 150, 300, 600, 700, 950, 1100, 1420])
time_vectorized = np.array([70, 40, 60, 130, 150, 170, 200, 225])
ax2 = fig.add_subplot(111)

# ax2 = fig.add_subplot(222)
ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"3 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()

# 4 задача

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([75, 1200, 14700, 120000, 367500, 1306800, 3630000, 15870000])
time_non_vectorized = np.array([550, 1330, 5300, 11320, 18100, 24500, 40500, 68300])
time_vectorized = np.array([80, 150, 230, 270, 310, 400, 460, 570])
ax2 = fig.add_subplot(111)


ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"4 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()

# 5 задача

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([200, 500, 1000, 2300, 3000, 5890, 7560, 10000])
time_non_vectorized = np.array([280, 200, 400, 970, 1110, 1550, 1890, 2370])
time_vectorized = np.array([310, 190, 230, 390, 450, 480, 610, 740])
ax2 = fig.add_subplot(111)

# ax2 = fig.add_subplot(222)
ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"5 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()

# 6 задача

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
fig = plt.figure()
data_size = np.array([80, 260, 640, 1080, 1760, 2600, 3320, 4360])
time_non_vectorized = np.array([2020, 13820, 45200, 102700, 230000, 483900, 875000, 1360000])
time_vectorized = np.array([440, 1100, 1530, 1890, 2400, 7980, 24700, 34900])
ax2 = fig.add_subplot(111)


ax2.plot(data_size, time_non_vectorized, label=u"Невекторизованная")
ax2.plot(data_size, time_vectorized, label=u"Векторизованная")
ax2.set_title(u"6 задача")
ax2.set_xlabel(u"Длина массива")
ax2.set_ylabel(u"Время (мкс)")
ax2.grid()
ax2.legend()

plt.show()
plt.close()
