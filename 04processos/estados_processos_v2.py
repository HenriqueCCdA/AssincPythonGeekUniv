import multiprocessing
import time
import ctypes


def funcao1(val, stat):
    if stat.value:
        res = val.value + 10
        stat.value = False
    else:
        res = val.value + 20
        val.value = 200
        stat.value = True

    print(f'O resultado dad função 1 é {res}')
    time.sleep(0.001)


def funcao2(val, stat):
    if stat.value:
        res = val.value + 30
        stat.value = False
    else:
        res = val.value + 40
        stat.value = True

    print(f'O resultado dad função 2 é {res}')
    time.sleep(0.001)


def main():
    valor = multiprocessing.Value('i', 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()