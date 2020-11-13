def first(n: int, it):
    iterador = iter(it)
    i = 0
    while i < n:
        try:
            aux = next(iterador)
            yield aux
            i += 1
        except StopIteration:
            return
    return


def filter(cond, it):
    iterador = iter(it)
    i = 0
    while True:
        try:
            aux = next(iterador)
            if cond(aux):
                yield aux
            i += 1
        except StopIteration:
            return

def take_while(cond,it):
    iterador = iter(it)
    i = 0
    while True:
        try:
            aux = next(iterador)
            if not cond(aux):
                return
            yield aux
            i += 1

        except StopIteration:
            return

def squares():
    i = 1
    while True:
        yield i*i
        i += 1


if __name__ == '__main__':

    print("EJERCICIO 5")

    prueba = first(100, squares())

    for i in prueba:
        print(i)

    prueba = take_while(lambda n: n < 100, squares())

    for i in prueba:
        print(i)

    print("cuac")
    prueba = filter(lambda n: str(n) == str(n)[::-1], squares())

    for i in range(20):
        next(prueba)



