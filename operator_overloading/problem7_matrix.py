"""Operator overloading - Problem 7.

Matrix class with the * operator overloaded for matrix multiplication.
"""


class Matrix:
    def __init__(self, rows):
        # rows is a list of lists, e.g. [[1, 2], [3, 4]]
        self.rows = rows
        self.n_rows = len(rows)
        self.n_cols = len(rows[0])

    def __mul__(self, other):
        # A (n x m) * B (m x p) is only defined if A has as many columns as B has rows
        if self.n_cols != other.n_rows:
            raise ValueError("Incompatible sizes: columns of A must equal rows of B")

        # Each cell (i, j) = sum of row i of A times column j of B
        result = []
        for i in range(self.n_rows):
            new_row = []
            for j in range(other.n_cols):
                total = 0
                for k in range(self.n_cols):
                    total += self.rows[i][k] * other.rows[k][j]
                new_row.append(total)
            result.append(new_row)
        return Matrix(result)

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return "\n".join(" ".join(f"{value:4}" for value in row) for row in self.rows)


if __name__ == "__main__":
    a = Matrix([[1, 2],
                [3, 4]])
    b = Matrix([[5, 6],
                [7, 8]])
    print("A =")
    print(a)
    print("B =")
    print(b)
    print("A * B =")
    print(a * b)  # [[19, 22], [43, 50]]
