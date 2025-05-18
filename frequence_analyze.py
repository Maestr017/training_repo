from collections import Counter
word = 'abababaaaaaadcfgdbbrw'
c = Counter(word).most_common()
print(c[0])