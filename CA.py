import numpy as np 
import matplotlib.pyplot as plt 

from rules import rule_1, rule_2, rule_3, rule_4

def main():
	space_dim = 45
	time_dim = 45
	image = np.zeros((time_dim, space_dim + 1), dtype='int32')
	image[0, (space_dim + 1)//2] = 1

	for t in range(1,time_dim):
		image[t] = rule_4(image[t-1])

	#print(image)
	#plt.figure(figsize = (8,6))
	plt.imshow(image, cmap='Greys', interpolation = "nearest")
	plt.savefig("Rule_4.png")
	plt.show()


if __name__ == "__main__":
	main()