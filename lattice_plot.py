import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

data = np.genfromtxt('lattice_output.txt')

fig = plt.figure(figsize=(8,8))                                                               
ax = fig.add_subplot(1,1,1)

markers = {1: 'o', 2: 'o'}
marker_colors = {1:'violet', 2:'blue'}

ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_ylabel('y [A]')
ax.set_xlabel('x [A]')
ax.set_xlim(min(data[2:,1])-1, max(data[2:,1])+1)
ax.set_ylim(min(data[2:,2])-1, max(data[2:,2])+1)

for i in range(2,len(data)):
	ax.errorbar(data[i,1], data[i,2], ls='None', marker=markers[data[i,3]], ms=12, color=marker_colors[data[i,3]], alpha=0.9)
	#ax.annotate(int(data[i,0]),xy=(data[i,1], data[i,2]))
	ax.text(data[i,1],data[i,2],int(data[i,0]), color='k', fontsize=12)
	for j in range(0,int(data[i,4])):
		line = Line2D([data[i,1],data[int(data[i,5+j])+1,1]],[data[i,2],data[int(data[i,5+j])+1,2]], linewidth=1, ls='-', color='grey', alpha=0.6)
		ax.add_line(line)

plt.savefig("lattice.pdf")
plt.show()
