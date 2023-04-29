s = input()

lower_case = ''.join(filter(lambda x: x.islower(), sorted(s)))
upper_case = ''.join(filter(lambda x: x.isupper(), sorted(s)))
odd = ''.join(filter(lambda x: int(x) % 2, filter(lambda y: y.isdigit(), sorted(s))))
even = ''.join(filter(lambda x: not int(x) % 2, filter(lambda y: y.isdigit(), sorted(s))))
print(lower_case + upper_case + odd + even)
