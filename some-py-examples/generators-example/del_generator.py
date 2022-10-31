class blabla(Exception):
    pass

def coroutine(f):
    def gen_func(*argp, **argn):
        g = f(*argp, **argn)
        next(g)
        return g
    return gen_func

# @coroutine  # убираем в случае использования yield from
def subgen():
    while True:
        try:
            message = yield
        except blabla:
            print("bla bla excaption")
        except StopIteration:
            break
        else:
            print(".............", message)
    return "returned from subgen()"

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except blabla as e:
    #         g.throw(e)
    result = yield from g
    print(result)
    # а нафига тогда делегирующий генератор нужен? если все выполняется на стороне подгенератора
    # для обработки возвращаемого значения с помощью return


if __name__ == '__main__':
    sg = subgen()
    g = delegator(sg)
    g.send("QKRQ")
    g.throw(blabla)
    g.send("QQ")
    g.throw(StopIteration)

