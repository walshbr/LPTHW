Things to know
#A comma seems to tell python that your code should all be treated as one line. 
#Ie. no new line at the end of a line that has a comma.

raw_input() 
#what you use to get input from the user

from sys import argv 
script, from_file, to_file = argv #example. The first one is just the name
# of the file you're using.
#Takes the argv function and imports it from sys to use in the program. 
#like loading in a gem.

open(filename, 'w')
#	opens a file in write mode

filename.truncate()
#	empties the file

filename.write(line)
#	writes the lines into the file.

filename.close()
#	closes and saves the file.

#white space is meaningful when writing functions. A function is written
def print_two(blah, blah):
	and then your internal code is indented one.

print file_name.read() # read the file
	

file_name.seek(a number)
#goes to a specific point in a file.

filename.readline()
#reads out the next line in a file as a string

#you have to return something at the end of a file
#
