import csv

d = {1: ['Craig Creager', 29], 
	 2: ['Judith Katzer', 57], 
	 3: ['Rowena Harris', 18], 
	 4: ['Shaun Alexander', 55], 
	 5: ['Natalie Vanhorn', 44]}


f = open('helloworld.csv','w')
for key in d:
	f.write("{},{},{}\n".format(key, d[key][0], d[key][1]))
f.close()