from collections import Counter, ChainMap


bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}


counter = Counter(input().split(','))
max_val = len(max(counter.keys(), key=len))
ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)

lines = []
res = 0
for key, val in sorted(counter.items()):
    line = f'{key.ljust(max_val)} x {val}'
    print(line)
    lines.append(len(line))
    res += ingredients[key] * val
last = f'ИТОГ: {res}р'
lines.append(len(last))
print('-' * max(lines))
print(f'ИТОГ: {res}р')


