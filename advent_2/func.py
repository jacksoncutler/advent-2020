def part1(input):
    res = 0
    for line in input:
        rules = line.split(':')[0].strip(' ')
        minMax = rules.split(' ')[0]

        min = int(minMax.split('-')[0])
        max = int(minMax.split('-')[1])
        letter = rules.split(' ')[1]
        str = line.split(':')[1].strip(' ')

        num = 0
        valid = True
        for char in str:
            if char == letter:
                num += 1
            if num > max:
                valid = False
                break
        if num < min:
            valid = False
        res += 1 if valid else 0
    return res


def part2(input):
    res = 0
    for line in input:
        rules = line.split(':')[0].strip(' ')
        minMax = rules.split(' ')[0]

        pos1 = int(minMax.split('-')[0])
        pos2 = int(minMax.split('-')[1])
        letter = rules.split(' ')[1]
        str = line.split(':')[1].strip(' ')

        num = 0
        valid = False
        for i in range(len(str)):
            for j in range(len(str)):
                if i+1 == pos1 and j+1 == pos2:
                    char1 = str[i]
                    char2 = str[j]
                    if (char1 == letter or char2 == letter) and char1 != char2:
                        valid = True
        res += 1 if valid else 0
    return res