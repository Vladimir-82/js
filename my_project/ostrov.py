import uuid
import pyshorteners
a = 'https://yandex.by/video/preview/?filmId=10086298432826588759&from=tabbar&parent-reqid=1657269212046069-14730982233553625529-sas3-0998-46d-sas-l7-balancer-8080-BAL-4085&text=%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81+%D1%81%D0%BE%D0%BA%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D1%8B%D1%85+%D1%81%D1%81%D1%8B%D0%BB%D0%BE%D0%BA+python+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81'

link = pyshorteners.Shortener().tinyurl.short(a)
print(link)


test = uuid.uuid1()
code = test.__str__()[:6]

print(''.join(('https://', 'mydomen/', code)))