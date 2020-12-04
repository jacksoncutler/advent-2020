def part1(input):
    for first in input:
        for second in input:
            if first + second == 2020:
                return first * second

def part2(input):
    for first in input:
        for second in input:
            for third in input:
                if first + second + third == 2020:
                    return first * second * third