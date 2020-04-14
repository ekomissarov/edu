def subgen_example():
    x = "Ready to accept message"
    message = yield x
    print("Subgen recived:", message)


def coroutine(f):
    def gen_func(*argp, **argn):
        g = f(*argp, **argn)
        next(g)
        return g
    return gen_func


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done!")
        else:
            count += 1
            summ += x
            average = round(summ/count, 2)

@coroutine
def average_with_return():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done!")
            break
        else:
            count += 1
            summ += x
            average = round(summ/count, 2)

    return average



if __name__ == '__main__':
    g = average()
    # g.send(None)  # next(g) - одно и то же взводим генератор


    print(g.send(4))
    print(g.send(5))

    g.throw(StopIteration)  # таким образом можно внутрь нашей корутины пробрасывать нужные нам исключения

    g1 = average_with_return()
    print(g1.send(4))
    print(g1.send(5))
    print(g1.send(4))
    print(g1.send(5))

    try:
        g1.throw(StopIteration)
    except StopIteration as e:
        print("Returned:", e.value, type(e), dir(e))

