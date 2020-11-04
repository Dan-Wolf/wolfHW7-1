def cb(x):
    return x*x*x

for i in range(20):
    if i % 2 == 1:
        print cb(i)
    else:
        print i

