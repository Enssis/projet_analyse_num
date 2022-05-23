from matr import matrice


def G(y, A, b):
    return (A * y - b).mult(2)


def rho_k(yk, A, b):
    Gyk = G(yk, A, b)
    if Gyk == 0:
        return 0
    return (Gyk.norme() ** 2) / (2 * Gyk.transpose() * A * Gyk).numb()


def gradient_a_pas_opti(n, y0):
    A = matrice(n, n)
    y = [y0]


if __name__ == '__main__':
    print('ui')
