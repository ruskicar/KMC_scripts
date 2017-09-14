#import numpy as np
#import matplotlib.pyplot as plt

reactions=[]

with open('mechanism_input.dat', 'r') as mechanism:
	for line in mechanism:
		if line.startswith('step '):
			reactions.extend([line[5:-1],0])
		if line.startswith('reversible_step '):
			reactions.extend([line[16:-1]+"_fwd",0])
			reactions.extend([line[16:-1]+"_rev",0])
	with open('general_output.txt', 'r') as file1:
		for line1 in file1:
			if line1.startswith('   Elementary step '): reactions[reactions.index(line1[19:-1])+1]+=1

print "#",
for k in range(0,len(reactions)/2): print reactions[::2][k],
print '\n',
for k in range(0,len(reactions)/2): print str(reactions[1::2][k]),
