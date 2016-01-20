#Inclass exercise 3

import numpy as np
from matplotlib import pyplot as plt

def plot():
	x = np.linspace(0, 2*np.pi, 100)
	y, z = np.sin(x), np.cos(x)
	
	fig = plt.figure()

	ax1 = fig.add_subplot(211)
	ax1.plot(y, "r")
	ax1.plot(z, "b")

	plt.xlabel("% of Period")
	plt.ylabel("Y-Value")
	plt.title("Plotting sin and cos with lines")

	ax2 = fig.add_subplot(212)
	ax2.plot(y, "ro")
	ax2.plot(z, "b^")

	plt.xlabel("% of Period")
        plt.ylabel("Y-Value")
	plt.title("Plotting sin and cos with shapes")

	plt.show()

if __name__ == "__main__":
	plot()
