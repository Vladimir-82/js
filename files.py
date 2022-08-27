def solution(a, b):
    res = sorted([a, b], key=len)
    return ''.join((res[0], res[1], res[0]))


print(solution('45', '1'))