import time
a, b = map(int, input("Input two numbers: ").split())


def inv(a, b):
    g = [b, a]
    u = [1, 0]
    v = [0, 1]
    y = [0, 0]
    i = 1

    while g[i] != 0:
        y.append(int(g[i-1]/g[i]))
        g.append(g[i-1]-y[i+1]*g[i])
        u.append(u[i-1]-y[i+1]*u[i])
        v.append(v[i-1]-y[i+1]*v[i])
        i = i+1

    if v[i-1] < 0:
        v[i-1] = v[i-1] + b
    x = v[i-1]

    if (a*x) % b != 1:
        print("Inverse does not exist")
    return x


t0 = time.time()
x = inv(a, b)
t1 = time.time()
print(x)
print(t1-t0)
