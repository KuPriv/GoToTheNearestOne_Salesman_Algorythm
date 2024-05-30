from algorythm import create_matrix, fill_matrix, go_to_neighbor, print_matrix, full_check, read_from_file
import time


def main():
    w = int(input("Прочитать с файла - 1 /// или сгенерировать матрицу - 0: "))
    if w == 0:
        n = int(input("Введите кол-во городов: "))
        a = create_matrix(n)
        fill_matrix(a, n)
    if w == 1:
        n, a = read_from_file()
    w = int(input("Иди в ближайший - 1 /// Полный перебор - 0: "))
    if w == 1:
        go_to_neighbor(a, n)
    if w == 0:
        full_check(a, n)
    w = int(input("Напечать матрицу? 1 - ДА, 0 - НЕТ: "))
    if w == 1:
        print_matrix(a, n)
    else:
        ...
    print('Спасибо, я пошел...')


if __name__ == "__main__":
    main()