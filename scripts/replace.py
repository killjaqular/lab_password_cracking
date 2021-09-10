"""
Author:  Adonay Pichardo
Date:    07SEP2021
Contact: apichardo2019@my.fit.edu
"""

from sys import argv # Used for command line arguments

old_file = open(argv[1], "r")                               # The original dictionary
new_file = open("../dictionaries/" +\
		   argv[0][:-3] + argv[2] + argv[3] + ".dict", "w") # The new altered dictionary

for every_line in old_file.readlines():
	if argv[2] in every_line:
		every_line = every_line.replace(argv[2], argv[3])
		new_file.write(every_line)

old_file.close()
new_file.close()
