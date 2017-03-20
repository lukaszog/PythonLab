import timeit
from time import time

string = "hello"

t = time()
nowy = ""
for l in string:
    nowy = l + nowy
print nowy
print time()-t

print timeit.timeit('"tojestnapis"[::-1]', number=100000)

print timeit.timeit('"".join(reversed("tojestnapis"))', number=100000)

print ''.join(reversed(string))

