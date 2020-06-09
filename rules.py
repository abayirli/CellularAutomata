#CA rules degined by numbers
import numpy as np 

def rule_1(row):
	"""Cell i becomes (or stays) black if one or more of 
	the triad [i-1, i, i+1] is black; 
	otherwise it stays (or becomes) white"""

	new_row = np.zeros(row.shape[0])
	for i, cel in enumerate(row):
		if(row[i-1] + row[i] + row[(i+1) % len(row)] >= 1):
			new_row[i] = 1
		else:
			new_row[i] = 0
	return new_row

def rule_2(row):
	"""Cell i becomes (or stays) black if either or both of its
	neighbors i-1 and i+1 are black; 
	otherwise it stays (or becomes) white"""

	new_row = np.zeros(row.shape[0])
	for i, cel in enumerate(row):
		if(row[i-1] + row[(i+1) % len(row)] >= 1):
			new_row[i] = 1
		else:
			new_row[i] = 0
	return new_row

def rule_3(row):
	""" Cell i becomes (or stays) black if one and only one
	of its neighors i-1 and i+1 is black;
	otherwise it stays (or becomes) white"""

	new_row = np.zeros(row.shape[0])
	for i, cel in enumerate(row):
		if(row[i-1] + row[(i+1) % len(row)] == 1):
			new_row[i] = 1
		else:
			new_row[i] = 0
	return new_row

def rule_4(row):
	""" Cell i becomes (or stays) black if one and only one
	of the triad [i-1, i, i+1] is black or if only i and i+1 are black;
	otherwise it stays (or becomes) white"""

	new_row = np.zeros(row.shape[0])
	for i, cel in enumerate(row):
		if((row[i-1] + row[i] + row[(i+1) % len(row)] == 1) or 			#only one of the triad is black
		   ((row[i] + row[(i+1) % len(row)] == 2) and row[i-1] == 0)):	#only i and i+1 is black, i-1 i white
			new_row[i] = 1
		else:
			new_row[i] = 0
	return new_row