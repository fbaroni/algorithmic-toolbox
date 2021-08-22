import matplotlib.pyplot as plt
import numpy as np

import math
n = np.linspace(2, 7)
plt.plot(n, n**3, label="n**3")
plt.plot(n, n**0.3, label="n**0.3")
plt.plot(n, n, label="n")
plt.plot(n, np.sqrt(n), label="sqrtn")
plt.plot(n, (n ** 2) / np.sqrt(n), label="(n ** 2) / np.sqrt(n)")
plt.plot(n, n ** 2, label="n **2")
 
plt.plot(n, 3**n, label="3**n")
plt.plot(n, n * np.log2(n), label="n * np.log2(n)")
plt.plot(n, np.log(n) / np.log(4), label="log4n")
plt.plot(n, 5 ** (np.log2(n)), label="5 ** (np.log2(n))")
plt.plot(n, n, label="n")
plt.plot(n, np.sqrt(n), label="sqrtn")
plt.plot(n, 2 ** (2*n), label="2 ** (2*n)")
plt.plot(n, n ** 2, label="n ** 2")
plt.legend(loc='upper left')
plt.show()