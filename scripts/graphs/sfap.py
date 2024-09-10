import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from signals import mono, bi, tri, tetra
# Load the data from CSV files
sfap2 = pd.read_csv('sfap2.csv').values
sfap5 = pd.read_csv('sfap5.csv').values
sfap10 = pd.read_csv('sfap10.csv').values

totalAxons = 10000
lambda_ = 100

cnap = np.zeros((5, 1300))
shiftSfap10 = np.zeros((5, 140 + sfap10.shape[1]))

# adjust the indexing to ensure correct broadcasting
shiftSfap10[0, 60:60 + sfap10.shape[1]] = sfap10[0, :]
shiftSfap10[1, 80:80 + sfap10.shape[1]] = sfap10[1, :]
shiftSfap10[2, 100:100 + sfap10.shape[1]] = sfap10[2, :]
shiftSfap10[3, 120:120 + sfap10.shape[1]] = sfap10[3, :]
shiftSfap10[4, 140:140 + sfap10.shape[1]] = sfap10[4, :]

poisson = np.random.poisson(lambda_, int(totalAxons * 0.4))
for i in range(int(totalAxons * 0.4)):
    offset = poisson[i]
    if offset + shiftSfap10.shape[1] <= cnap.shape[1]:
        cnap[:, offset:offset + shiftSfap10.shape[1]] += shiftSfap10

poisson = np.random.poisson(lambda_, int(totalAxons * 0.6))
for i in range(int(totalAxons * 0.6)):
    offset = poisson[i]
    if offset + sfap5.shape[1] <= cnap.shape[1]:
        cnap[:, offset:offset + sfap5.shape[1]] += sfap5

cnap *= 1000
cnap = cnap[:, :800]

plt.figure("Overlayed Signals")

# Monopolar
plt.plot(mono(0, cnap), label="Monopolar 1", linestyle='-', linewidth=2)
# Bipolar
plt.plot(bi(0, 1, cnap), label="Bipolar 1-2", linestyle='-.')
# Tripolar
plt.plot(tri(0, 1, 2, cnap), label="Tripolar 1-2-3", linestyle='-.')
# Tetrapolar
plt.plot(tetra(0, 1, 2, 3, cnap), label="Tetrapolar 1-2-3-4", linestyle='-',linewidth=2)

# Formatting the plot
plt.xlabel("Time (ms)")
plt.ylabel("V (μV)")
plt.legend()
plt.show()