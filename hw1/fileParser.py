import sys
import os

to_write_file_pointer = open('to_read.txt', 'w')

for number in range(1, 10):
    to_write_file_pointer.write("{0}\n".format(number))

letters = ['a', 'b', 'c', 'd', 'e']

for letter in letters:
    to_write_file_pointer.write("{0}\n".format(letter))


to_write_file_pointer.close()


to_read_file_pointer = open('to_read.txt', 'r')

for line in to_read_file_pointer:
    print("Line: {0}".format(line))

to_read_file_pointer.close()


os.remove("to_read.txt")
raise SystemExit(0)