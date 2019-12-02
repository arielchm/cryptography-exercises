import time

# Find all prime numbers in the range (a,b)
a = 1000000000
b = 1000000100


def fermat_primality_test(a, b):
    if a % 2 == 0:
        a += 1
    for i in range(a, b, 2):
        k = i-1
        if pow(2, k, i) == 1 and pow(3, k, i) == 1 and pow(5, k, i) == 1 and pow(7, k, i) == 1:
            print(i)


n = int(input())
for i in range(n):
    #a,b =map(int, input().split())
    time0 = time.time()
    fermat_primality_test(a, b)
    time1 = time.time()
    print(time1-time0)
