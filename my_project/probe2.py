def sourcetemplate(url):
    def func(**kwargs):
        dc = {}
        res = url
        if not kwargs:
            return url
        else:
            res += '?'
            counter = 0
            for key, val in kwargs.items():
                dc.setdefault(key, val)
            for key, val in sorted(dc.items(), key=lambda x: x[0]):
                res += key + '=' + str(val)
                counter += 1
                if counter < len(dc):
                    res += '&'
        return res
    return func

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

# https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165
# https://stepik.org/lesson/651459/step/14?thread=solutionsunit=648165