import sys
import os

file_pointer = open('initial.txt', 'w+')
output_file = open('output.txt', 'w')

for number in range(1, 10):
    file_pointer.write("{0}\n".format(number))

letters = ['a', 'b', 'c', 'd', 'e']

for letter in letters:
    file_pointer.write("{0}\n".format(letter))

file_pointer.seek(0,0)

for line in file_pointer:
    #print("Line: {0}".format(line))
    output_file.write("Line: {0}".format(line))

file_pointer.close()
output_file.close()

#os.remove("to_read.txt")
raise SystemExit(0)