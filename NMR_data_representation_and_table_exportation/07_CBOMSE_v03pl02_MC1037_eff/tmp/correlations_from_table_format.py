text = """
2.78	0.92, 4.35, 5.32, 7.75, 9.28
0.92	2.78, 4.35, 5.32
4.35	0.92, 2.78, 6.09
7.75	2.78
5.32	0.92, 1.55, 2.78
6.09	4.35, 5.45
-	-
1.55	2.56, 5.32, 5.45s, 7.19
5.45	0.98, 1.55s, 2.56, 2.68, 2.74, 3.25, 6.09
2.56	0.98, 1.55, 3.19, 3.25, 5.45
0.98	2.56, 2.74, 3.19, 3.25, 5.45
3.25	0.98, 2.56, 2.68, 2.74, 5.45, 7.19
3.19	0.98, 2.56, 2.68, 2.74, 7.19
2.74	0.98, 3.19, 3.25, 5.45, 7.19
2.68	3.19, 3.25, 5.45, 7.19
-	-
7.19	1.55, 2.68, 2.74, 3.19, 3.25
7.27	-
7.18	-
"""


#print text.split('\n')#.remove('')

#for l in text.split('\n').remove(''):
#    print '*', l

data = [e for e in text.replace(',', '').split('\n') if e]
#print data

correlations = []

for l in data:
    #print l
    [a, b] = l.split('\t')[0], l.split('\t')[1]
    print a, '*', b
    for e in b.split():
        print a, e
        c=sorted([a,e])
        correlations.append(c[0]+'*'+c[1])
        

#print correlations
print len(correlations)
print len(set(correlations))
print set(correlations)
for e in set(correlations):
    #print e.split('*')
    print e.replace('*', '\t')





