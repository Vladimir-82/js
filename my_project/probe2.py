import re

def func(poses, string):
    pos, endpos = int(poses.split()[0]), int(poses.split()[1])
    regex_obj = re.compile(r'\d+')
    result = list(regex_obj.findall(string, pos=pos, endpos=endpos))
    return sum([int(i) for i in result])



poses = input()
string = input()

print(func(poses=poses, string=string))







