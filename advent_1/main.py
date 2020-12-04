from func import *

input = []
file = open('input.txt')
line = file.readline(16)
while line:
    input.append(int(line))
    line = file.readline()

print(part1(input))
print(part2(input))