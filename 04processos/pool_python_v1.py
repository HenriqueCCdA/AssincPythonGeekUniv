import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    tamanaho_pool = multiprocessing.cpu_count() * 2

    print(f'Tamanho da Pool: {tamanaho_pool}')

    pool = multiprocessing.Pool(processes=tamanaho_pool)

    entradas = list(range(7))

    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()