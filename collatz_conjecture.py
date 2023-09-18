import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
def f(n):
    r = []
    while n != 1:
        r.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    return r
r = f(10011)
print(r)
plt.plot(r)
plt.show()
