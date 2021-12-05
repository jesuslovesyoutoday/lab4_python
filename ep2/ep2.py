from scipy import linalg
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

files = ['small.txt', 'large.txt']

def solve(i, filename):
	with open(filename, 'r') as f:
		l = [[float(num) for num in line.split(' ')] for line in f]

	n = int(l[0][0])
	A = l[1:n+1]
	b = l[n+1:][0]

	x = linalg.solve(A, b)
	print(x)

	objects = np.linspace(0, n, n)

	y_pos = np.arange(len(objects))
	performance = x

	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks()
	plt.grid()

	#plt.show()
	plt.savefig(str(i+1)+'.png')

for i in range(len(files)):
	solve(i, files[i])
