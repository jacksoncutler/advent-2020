from func import *

input = []
file = open('input.txt')
line = file.readline()
while line:
    input.append(line.strip('\n'))
    line = file.readline()

print(part1(input))
print(part2(input))