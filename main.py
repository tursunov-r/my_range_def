from test_time import time_decorator


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


@time_decorator
def test_my_range(start, stop, step):
    for i in my_range(start, stop + 1, step):
        if i == stop:
            print(f"strat -> {start}, stop -> {stop}, step -> {step}")

@time_decorator
def test_default_range(start, stop, step):
    for i in range(start, stop + 1, step):
        if i == stop:
            print(f"strat -> {start}, stop -> {stop}, step -> {step}")

test_my_range(1, 10_000_000, 1)
test_default_range(1, 10_000_000, 1)