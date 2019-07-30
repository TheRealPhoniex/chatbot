import csv
from itertools import chain

with open('nice_words.csv', 'r') as f:
   reader = csv.reader(f)
   good_expressions = list(reader)
   #good_expressions = list(chain(reader))
   #good_expressions =str(good_expressions)[1:-1]

##print(your_list)


import re
list = good_expressions
string = re.sub('[\[\]]','',repr(list))
print(string)

#good_expressions  = list(reader)
#good_expressions  = list(chain(good_expressions))

#print(good_expressions)