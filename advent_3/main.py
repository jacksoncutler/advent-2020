from func import *

file = open('input.txt')
line = file.readline()
input = []
while line:
    input.append(line.strip('\n'))
    line = file.readline()


print(
    func(input, 1, 1) *
    func(input, 3, 1) *
    func(input, 5, 1) *
    func(input, 7, 1) *
    func(input, 1, 2)
)