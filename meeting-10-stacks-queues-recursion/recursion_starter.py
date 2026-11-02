
def countdown(n):
if n == 0:
    print("Blast off!")
    return

print(n)

countdown(n - 1)

print("Returning from:", n)

countdown(10)
