import re

def func(input):
    res = 0
    for passport in input:
        complete = True
        p_arr = passport.strip(' ').split(' ')
        if len(p_arr) <= 6:
            complete = False
        elif len(p_arr) == 7:
            for field in passport.split(' '):
                if field.split(':')[0] == 'cid':
                    complete = False
                    break
        if complete:
            valid = True
            for field in p_arr:
                key = field.split(':')[0]
                val = field.split(':')[1].strip(' ')
                if key == 'byr':
                    if len(val) != 4 or int(val) < 1920 or int(val) > 2002:
                        valid = False
                        break
                if key == 'iyr':
                    if len(val) != 4 or int(val) < 2010 or int(val) > 2020:
                        valid = False
                        break
                if key == 'eyr':
                    if len(val) != 4 or int(val) < 2020 or int(val) > 2030:
                        valid = False
                        break
                if key == 'hgt':
                    system = re.findall(r'[a-z]*$', val)[0]
                    number = int(re.findall(r'^[0-9]*', val)[0])
                    if system == 'cm':
                        if number < 150 or number > 193:
                            valid = False
                            break
                    elif system == 'in':
                        if number < 59 or number > 76:
                            valid = False
                            break
                    else:
                        valid = False
                        break
                if key == 'hcl':
                    if val[0] != '#':
                        valid = False
                        break
                    val = val.strip('#')
                    if len(val) != 6 or re.findall(r'[^0-9a-f]', val) != []:
                        valid = False
                        break
                if key == 'ecl':
                    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if val not in colors:
                        valid = False
                        break
                if key == 'pid':
                    if len(val) != 9:
                        valid = False
                        break
            if valid:
                res += 1
    return res

