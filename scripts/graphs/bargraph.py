import numpy as np
import matplotlib.pyplot as plt
from signals import mono, bi, tri, tetra, vpp
# Assuming vpp, mono, bi, tri, tetra, and cnap are defined elsewhere in your code

barGraph = np.array([
    [vpp(mono(1, cnap)), vpp(mono(2, cnap)), vpp(mono(3, cnap)), vpp(mono(4, cnap)), vpp(mono(5, cnap))],
    [(vpp(bi(1, 2, cnap)) + vpp(bi(1, 3, cnap)) + vpp(bi(1, 4, cnap)) + vpp(bi(1, 5, cnap))) / 4,
     (vpp(bi(1, 2, cnap)) + vpp(bi(2, 3, cnap)) + vpp(bi(2, 4, cnap)) + vpp(bi(2, 5, cnap))) / 4,
     (vpp(bi(1, 3, cnap)) + vpp(bi(2, 3, cnap)) + vpp(bi(3, 4, cnap)) + vpp(bi(3, 5, cnap))) / 4,
     (vpp(bi(1, 4, cnap)) + vpp(bi(2, 4, cnap)) + vpp(bi(3, 4, cnap)) + vpp(bi(4, 5, cnap))) / 4,
     (vpp(bi(1, 5, cnap)) + vpp(bi(2, 5, cnap)) + vpp(bi(3, 5, cnap)) + vpp(bi(4, 5, cnap))) / 4],
    [(vpp(tri(1, 2, 3, cnap)) + vpp(tri(1, 3, 5, cnap))) / 2,
     (vpp(tri(1, 2, 3, cnap)) + vpp(tri(2, 3, 4, cnap))) / 2,
     (vpp(tri(1, 2, 3, cnap)) + vpp(tri(2, 3, 4, cnap)) + vpp(tri(3, 4, 5, cnap)) + vpp(tri(1, 3, 5, cnap))) / 4,
     (vpp(tri(2, 3, 4, cnap)) + vpp(tri(3, 4, 5, cnap))) / 2,
     (vpp(tri(1, 3, 5, cnap)) + vpp(tri(3, 4, 5, cnap))) / 2],
    [vpp(tetra(1, 2, 3, 4, cnap)),
     (vpp(tetra(1, 2, 3, 4, cnap)) + vpp(tetra(2, 3, 4, 5, cnap))) / 2,
     (vpp(tetra(1, 2, 3, 4, cnap)) + vpp(tetra(2, 3, 4, 5, cnap))) / 2,
     (vpp(tetra(1, 2, 3, 4, cnap)) + vpp(tetra(2, 3, 4, 5, cnap))) / 2,
     vpp(tetra(2, 3, 4, 5, cnap))]
])

x = ["Monopolar", "Bipolar", "Tripolar", "Tetrapolar"]
fig, ax = plt.subplots()

bar_width = 0.10
spacing = 0.15  # Increase this value to add more space between groups
positions = np.arange(len(x)) * (bar_width * 5 + spacing)

# Define colors for each set of bars
colors = ['#487de7', '#ffa500', '#79c314', '#e81416', '#70369d']

# Plot each set of bars with specified colors
for i in range(5):
    ax.bar(positions + i * bar_width, barGraph[:, i], bar_width, label=f'V{i+1}', color=colors[i], alpha=0.7)

ax.set_xticks(positions + bar_width * 2)
ax.set_xticklabels(x)

ax.set_ylabel("Vpp (μV)")
ax.legend()
plt.show()