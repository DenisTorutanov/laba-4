import random
import time

def print_matrix(M,matr_name,tt):
        print ("матрица "+matr_name+" промежуточное время = " +str(format(tt, '0.2f'))+ " seconds.")
        for i in M:            # делаем перебор всех строк матрицы
            for j in i:     # перебираем все элементы в строке
                print("%5d" % j, end=' ')
            print()

try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К = "))
    start = time.time()
    A,F,AT,AF = [],[],[] ,[]                    # задаем матрицы
    for i in range(row_q):
        A.append([0]*row_q)
        F.append([0]*row_q)
        AT.append([0]*row_q)
        AF.append([0]*row_q)
    time_next = time.time()
    print_matrix(F,"F",time_next-start)

    for i in range(row_q):      # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10,10)
    time_prev = time_next
    time_next = time.time()
    print_matrix(A,"A",time_next-time_prev)

    for i in range(row_q):      # создаем матрицу F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"F",time_next-time_prev)

    E = []  # задаем матрицу E
    size = row_q // 2
    for i in range(size):
        E.append([0] * size)

    for i in range(size):  # формируем подматрицу E
        for j in range(size):
            E[i][j] = F[size + i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)

    cnt = 0
    sum = 1
    for i in range(size):  # работаем с подматрицей E
        for j in range(size):
            if j % 2 == 0 and i < j and j > size - 1 - i and E[i][j] > K:
                cnt += 1
            elif j % 2 != 0 and i > j and j < size - 1 - i:
                sum += E[i][j]

    if cnt > sum:
        for i in range(1, size // 2, 1):  # меняем подматрицу E
            for j in range(0, i, 1):
                E[i][j], E[i][size - j - 1] = E[i][size - j - 1], E[i][j]
        for i in range(size // 2, size, 1):
            for j in range(0, i, 1):
                E[i][j], E[i][size - j - 1] = E[i][size - j - 1], E[i][j]
        print_matrix(E, "E", time_next - time_prev)
        for i in range(size):           # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = E[i][j]
    else:
        for i in range(row_q // 2):
            for j in range(0, row_q // 2):
                F[i][j], F[i][row_q // 2 + row_q % 2 + j] = F[i][row_q // 2 + row_q % 2 + j], F[i][j]

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):          # Умножение матрицы F на матрицу A
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
                AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "F*A", time_next - time_prev)

    for i in range(row_q):          # Транспонирование матрицы A
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):          # Умножение числа K на транспонированную матрицу A
        for j in range(row_q):
            A[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A^T", time_next - time_prev)

    for i in range(row_q):          # A*F–K*AT
        for j in range(row_q):
            AF[i][j] = AF[i][j]-K*AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "A*F–K*AT ", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Время работы программы: " + str(result) + " секунд.")

except ValueError:
     print("\nЭто не число.")

except FileNotFoundError:
     print(
         "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
