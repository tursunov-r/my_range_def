def my_range(*args):
    mode = len(args)
    if mode == 1:
        start = 0
        stop = args[0]
        step = 1
    elif mode == 2:
        start = args[0]
        stop = args[1]
        step = 1 if start < stop else -1
    elif mode == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if step == 0:
            raise ValueError("Step cannot be zero")
    else:
        raise TypeError(f"my_range expected 1 to 3 arguments, got {mode}")

    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step


print(f"just 1 arg")
for i in my_range(10):
    print(i)

print("2 args")
for i in my_range(1, 10):
    print(i)

for i in my_range(10, 1):
    print(i)

print("3 args")
for i in my_range(1, 10, 2):
    print(i)

for i in my_range(100, 10, -10):
    print(i)
