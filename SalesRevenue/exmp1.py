import random

# 8475, 9281, 7000, 5855, 9635, 5653, 5935, 5000, 4161, 5222, 5329, 1399

lst = [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
lst1 = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
s2 =  "flowchart TD\n  A[Christmas] -->|Get money| B(Go shopping)\n  B --> C{Let me think}\n  C -->|One| D[Laptop]\n  C -->|Two| E[iPhone]\n  C -->|Three| F[fa:fa-car Car]"
s1 = 'xychart-beta\n  title "Sales Revenue"\n  x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]\n  y-axis "Revenue (in $)" 4000 --> 11000\n  bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]\n  line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]'
s3 = f'xychart-beta\n  title "Sales Revenue"\n  x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]\n  y-axis "Revenue (in $)" 4000 --> 11000\n  line {lst}'
s = """
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
"""
# print(s3)
# d = {}
# for i in lst1:
#     d.setdefault(i,4000)
#
# print(d)
# print([4000]*12)
a = [random.randint(0,11000) for _ in range(12)]
print(a, sep=",")