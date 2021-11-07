def Merge(d1, d2):
    return(d2.update(d1))
d1 = {'a': 1, 'b': 6}
d2 = {'d': 5, 'c': 3}
Merge(d1, d2)
print(d2)