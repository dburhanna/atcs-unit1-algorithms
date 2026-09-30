def constant_work(n):
    return 1

def linear_work(n):
    operations=0
    for _ in range(n): operations+=1
    return operations

def quadratic_work(n):
    operations=0
    for _ in range(n):
        for _ in range(n): operations+=1
    return operations

for n in [10,100,1000]:
    print(n, constant_work(n), linear_work(n), quadratic_work(n))
