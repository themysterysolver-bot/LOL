from collections import defaultdict,Counter

text = """
I am R.Prabhakara Arjun. I am currently pursuing my bachelor's degree
in MIT. This is a map reduce program. Which will break down using map and reduce using combining logic.
In the end we would get to see the end as single extension of counter. Counter is a python inbuilt function which directly finds
the frequency. 
"""

def map(text):
    words=text.lower().replace('.', '').replace(',', '').split()
    mapper=[]
    for word in words:
        mapper.append((word, 1))
    return mapper

def group(mapper):
    grouped = defaultdict(list)
    for w,c in mapper:
        grouped[w].append(c)
    print(grouped)
    return grouped

def reduce(grouped):
    reduced = {}
    for word, counts in grouped.items():
        reduced[word] = sum(counts)
    return reduced

M_data = map(text)
grouped_data = group(M_data)
r_d = reduce(grouped_data)

print('USING MAP REDUCE:')
for key,val in sorted(r_d.items()):
    print(key,":",val)

#implementing usng single Counter
print('USING COUNTER:')
for key,val in sorted(r_d.items()):
    print(key,":",val)
