class Matrice:

    ## n est le nombre de lignes
    ## m est le nombre de colonnes

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrice = [[0.0 for j in range(m)] for i in range(n)]

    def __str__(self):
        return str(self.matrice)

    def __add__(self, other):
        if self.n == other.n and self.m == other.m:
            result = Matrice(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.matrice[i][j] = self.matrice[i][j] + other.matrice[i][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __sub__(self, other):
        if self.n == other.n and self.m == other.m:
            result = Matrice(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.matrice[i][j] = self.matrice[i][j] - other.matrice[i][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __mul__(self, other):
        if self.m == other.n:
            result = Matrice(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        result.matrice[i][j] += self.matrice[i][k] * other.matrice[k][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __eq__(self, other):
        if self.n == other.n and self.m == other.m:
            for i in range(self.n):
                for j in range(self.m):
                    if self.matrice[i][j] != other.matrice[i][j]:
                        return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, i, j):
        return self.matrice[i][j]

    def __setitem__(self, i, j, value):
        self.matrice[i][j] = value

    def __delitem__(self, i, j):
        del self.matrice[i][j]

    def set_diag(self, value):
        for i in range(self.n):
            self.matrice[i][i] = value


