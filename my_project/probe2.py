from regex import findall as f


s = 'Peter: (313) 555-1234'

# reg = r'(\(\d{3}\)|\d{3}) (0|-)(\d{3}-\d{4})'
reg = r'(\([2-9]\d{2}\)|[2-9]\d{2})'

result = f(reg, s)

[print(i) for i in result]
