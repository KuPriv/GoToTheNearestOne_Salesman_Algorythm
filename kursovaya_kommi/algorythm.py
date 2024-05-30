import random
import sys
import time
from copy import copy
from sys import setrecursionlimit


def read_from_file():
    r = int(input("Какой файл читаем? 10 городов - 1, 11 городов - 2: "))
    if r == 1:
        with open('1.txt') as F:
            data = F.readlines()
    if r == 2:
        with open('2.txt') as F:
            data = F.readlines()
    F.close()
    n = int(data[0])
    data: list[int] = [line.rstrip() for line in data[1:]]
    a = [[int(x) for x in data[i].split()] for i in range(n)]
    return n, a


def create_matrix(n: int) -> list[list[int]]:
    return [[0 for j in range(n)] for i in range(n)]


def print_matrix(a: list[list[int]], n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()


def fill_matrix(a: list[list[int]], n: int) -> list[list[int]]:
    for i in range(n):
        for j in range(i, n):
            if i != j:
                a[i][j] = a[j][i] = random.randint(1, 100)


def go_to_neighbor(a: list[list[int]], n: int) -> None:
    q = int(input(f"Введите начальный город <= {n}: ")) - 1
    list_of_sums: list[int] = [0] * n
    way: list[int] = [-1] * n
    position_way: int = 0
    way[position_way] = q
    sum_of_ways: int = 0
    start_time = time.time()
    setrecursionlimit(10000)
    res = recursion_way_for_fastmethod(a, n, sum_of_ways, way, position_way, q, list_of_sums)
    print(f'Время выполнения алгоритма: {time.time() - start_time}')
    last_list = res.get('ls')
    last_sum = res.get('sum')
    last_way = res.get('way')
    print("Лучший маршрут:")
    last_way = [i + 1 for i in last_way]
    print(f'Длина маршрута= {last_sum} Путь: {last_way}, Список длин: {last_list}')


def recursion_way_for_fastmethod(a: list[int], n: int, summ: int, way: list[int], position_way: int, q: int, list_of_sums: list[int]) -> dict[str]:
    if position_way + 1 == n:
        way.append(way[0])
        summ += a[-1][0]
        list_of_sums[-1] += a[-1][0]
        res: dict[str] = {'way': way, 'sum': summ, 'ls': list_of_sums}
        return res
    mi: int = sys.maxsize
    need_index: int = -1
    a_str: list[int] = a[q]
    for i in range(n):
        if a_str[i] <= mi and a_str[i] != 0 and (i not in way):
            mi = a_str[i]
            need_index = i
    list_of_sums[position_way] = a_str[need_index]
    position_way += 1
    way[position_way] = need_index
    summ += a_str[need_index]
    q = need_index
    return recursion_way_for_fastmethod(a, n, summ, way, position_way, q, list_of_sums)


k = 0
max_sum = 0
list_of_sums = []


def create_matrix_for_full(n, q):
    a = [i + 1 for i in range(n)]
    s = a.index(q)
    a[0], a[s] = a[s], a[0]
    return a


def recursion_for_full(a: list[int], n: int, q: int, way: list[int]):
    global k
    k += 1
    if q >= n:
        global last_way
        global max_sum
        global list_of_sums
        if k == n:
            max_sum = sys.maxsize
        sum_of_ways: int = 0
        for i in range(1, n):
            sum_of_ways += a[way[i - 1] - 1][way[i] - 1]
        sum_of_ways += a[way[-1] - 1][way[0] - 1]
        if sum_of_ways <= max_sum:
            max_sum = sum_of_ways
            last_way = copy(way)
            list_of_sums = [0] * n
            for i in range(1, n):
                list_of_sums[i - 1] = a[way[i - 1] - 1][way[i] - 1]
            list_of_sums[-1] = a[way[-1] - 1][way[0] - 1]
        return 0
    recursion_for_full(a, n, q + 1, way)
    i = q + 1
    for i in range(i, n):
        way[i], way[q] = way[q], way[i]
        recursion_for_full(a, n, q + 1, way)
        way[i], way[q] = way[q], way[i]


def full_check(a: list[list[int]], n: int) -> None:
    q = int(input(f"Введите начальный город <= {n}: "))
    way = create_matrix_for_full(n, q)
    start_time = time.time()
    recursion_for_full(a, n, 1, way)
    print(f'Время выполнения алгоритма: {time.time() - start_time}')
    print("Лучший маршрут:")
    final_way = last_way
    final_way.append(last_way[0])
    print(f'Длина маршрута = {max_sum}, Путь = {final_way}, Список длин: {list_of_sums}')
