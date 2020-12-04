def func(input, xinc, yinc):
    col = 0
    res = 0
    for i in range(0, len(input), yinc):
        if i == 0:
            continue
        line = input[i]
        col += xinc
        if line[col % len(line)] == '#':
            res += 1
    return res
