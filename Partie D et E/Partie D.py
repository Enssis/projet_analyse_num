from matr import matrice


def G(y, A, b):
    return (A * y - b).mult(2)


def rho_k(yk, A, b):
    Gyk = G(yk, A, b)
    if Gyk.equal(0):
        return 0
    return (Gyk.norme() ** 2) / ((Gyk.transpose() * A * Gyk).numb() * 2)


def gradient_a_pas_opti(y0, maxi, epsilon, A, b):
    y = [y0]

    for i in range(maxi):
        yn = y[i] - G(y[i], A, b).mult(rho_k(y[i], A, b))
        y.append(yn)
        if (y[i + 1] - y[i]).norme() < epsilon:
            return y
    return y


def test_1():
    # fonction g2,2/7 de la partie C
    a = 2
    b = 2 / 7
    A = matrice(2, 2)
    A.values = [[1/a, 0],
                [0, 1/b]]

    b = matrice(2, 1)
    b.values = [[0], [0]]

    y0 = matrice(2, 1)
    y0.values = [[7], [1.5]]

    y = gradient_a_pas_opti(y0, 100, 10 ** -15, A, b)
    print(str(y[len(y) - 1])) # doit etre : (0, 0)
    print(len(y), "\n")


def test_2():
    A = matrice(3, 3)
    A.values = [[100, 10, 0],
                [10, 200, 10],
                [0, 10, 300]]

    b = matrice(3, 1)
    b.values = [[-100], [0], [300]]

    y0 = matrice(3, 1)
    y0.values = [[1], [1], [1]]

    y = gradient_a_pas_opti(y0, 100, 10 ** -10, A, b)
    print(str(y[len(y) - 1]))
    print(len(y), "\n")




if __name__ == '__main__':
    test_1()
    test_2()
