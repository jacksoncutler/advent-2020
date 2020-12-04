from func import *

input = []
file = open('input.txt')
line = file.readline()
passport = ''
while line:
    if line == '\n':
        input.append(passport)
        passport = ''
        line = file.readline()
        continue
    passport += ' ' + line.strip('\n')
    line = file.readline()

input.append(passport)

print(func(input))