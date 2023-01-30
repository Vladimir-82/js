import re
import sys

regex = r'((https*://)*([a-z\.]+\.[a-z]+/?))">(.*[a-zA-Z]+.*)</a>'
string = '<li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide">Beginner&#39;s Guide</a></li><li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/">Developer&#39;s Guide</a></li><li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/">FAQ</a></li><li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages">Non-English Docs</a></li><li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/">PEP Index</a></li><li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks">Python Books</a></li>'


result = re.finditer(regex, string)

for i in result:
    print(', '.join((i.group(1), i.group(4))), re.MULTILINE)



