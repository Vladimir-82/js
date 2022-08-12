def meeting(s):
    res = []
    splt = s.split(';')
    print(splt)
    for el in splt:
        res.append((el.split(':')[::-1]))
    print(res)

    return sorted(res, key=len)

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))


# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"