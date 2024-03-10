def iter_nums():
    for i in range(1489):
        yield i


iterator = iter_nums()

for i in iterator:
    print(str(i))



def func_get():
    i = 1

    while True:
        yield i
        i += 1

f = func_get()

print(next(f))


generator = (i for i in range(1489))

print(f)
print(next(f))
print(next(f))
def test_range():
    for i in range(0, 1):
        yield i

i = test_range()

print(next(i))



def outer_function():
    x = 10
    def inner_function():

        nonlocal x

        x += 1

        return x

    return inner_function()
function = outer_function()

print(function)




print(next(f))


def guard_zero(operate):

    def inner(x, y):

        if y == 0:
            print("cannot divide by zero")
            return

        return operate(x, y)
    return inner


@guard_zero
def devide(x, y):
    return x/y


print(devide(int(input()), int(input())))


print(f)






