
class Matrix:

    def __init__(self, rows, cols, matrix):
        self.rows = int(rows)
        self.cols = int(cols)
        self.matrix = list(matrix)
        self.dimensions = self.rows, self.cols

        # actual matrix is a list of lists:
        # [[1,2,3],
        #  [1,2,3],
        #  [1,2,3]]

    @classmethod
    def create(cls):
        # input matrix dimensions (rows then cols)
        # input format is 'row col'
        rows, cols = [int(ele) for ele in input('Enter rows and columns of matrix: ').split()]

        matrix = []
        # input matrix row by row with a space between each element
        print('Enter matrix row. Please leave a space between each element:')
        for i in range(rows):
            matrix.append([float(ele) for ele in input().split()])
        return cls(rows, cols, matrix)

    def print(self):
        # format each element correctly (justification, rounding, no negative zeroes)
        for row in range(self.rows):
            for col in range(self.cols):
                if float(self.matrix[row][col]) == -0.0:
                    self.matrix[row][col] = 0.0
                if not str(self.matrix[row][col]).startswith('-'):
                    self.matrix[row][col] = ' ' + str(self.matrix[row][col])

        # accept matrix stored as list then print elements in string form
        for row in range(self.rows):
            self.matrix[row] = ' '.join([str(ele) for ele in self.matrix[row]])
        self.matrix = '\n'.join(self.matrix)
        print('The result is:')
        print(self.matrix)


def matrix_add():
    # Add two matrices together

    # Check matrices are same size
    while True:
        mx_a = Matrix.create()
        mx_b = Matrix.create()
        if mx_a.dimensions != mx_b.dimensions:
            print('Matrices must have the same dimensions. Please input again')
            continue
        else:
            break

    mx_output = Matrix(mx_a.rows, mx_a.cols, [])

    for row in range(mx_output.rows):
        mx_output.matrix.append([])
        for col in range(mx_output.cols):
            mx_output.matrix[row].append(mx_a.matrix[row][col] + mx_b.matrix[row][col])

    mx_output.print()


def matrix_by_constant():
    # Multiply a matrix by a constant
    mx_a = Matrix.create()
    num = float(input('Enter constant: '))
    mx_output = Matrix(mx_a.rows, mx_a.cols, [])
    for row in range(mx_output.rows):
        mx_output.matrix.append([])
        for col in range(mx_output.cols):
            mx_output.matrix[row].append(str(float(mx_a.matrix[row][col]) * num))
    mx_output.print()


def matrix_by_matrix():
    # Multiply a matrix by a matrix
    while True:
        mx_a = Matrix.create()
        mx_b = Matrix.create()
        if mx_a.cols != mx_b.rows:
            print(
                'The columns of the first matrix must be equal to the rows of the second matrix. Please input again')
            continue
        else:
            break

    mx_output = Matrix(mx_a.rows, mx_b.cols, [])

    for row in range(mx_output.rows):
        mx_output.matrix.append([])
        for col in range(mx_output.cols):
            ele_sum = 0
            for i in range(mx_a.cols):
                ele_sum += float(mx_a.matrix[row][i]) * float(mx_b.matrix[i][col])
            mx_output.matrix[row].append(str(ele_sum))

    mx_output.print()


def matrix_transpose():
    transpose_choice = None
    while transpose_choice not in [0,1,2,3,4]:
        print('1. Main diagonal \n2. Side diagonal \n3. Vertical line \n4. Horizontal line')
        transpose_choice = int(input('Your choice: '))
        if transpose_choice == 1:
            transpose_main()
        elif transpose_choice == 2:
            transpose_side()
        elif transpose_choice == 3:
            transpose_vertical()
        elif transpose_choice == 4:
            transpose_horizontal()
        elif transpose_choice == 0:
            break
        else:
            print('Invalid choice, please try again')


def transpose_main():
    # Transpose a matrix along it's main diagonal
    mx_a = Matrix.create()
    mx_output = Matrix(mx_a.cols, mx_a.rows, [])

    for i in range(mx_output.rows):
        mx_output.matrix.append([])

    for col in range(mx_a.cols):
        for row in range(mx_a.rows):
            mx_output.matrix[col].append(mx_a.matrix[row][col])

    mx_output.print()


def transpose_side():
    # Transpose a matrix along it's side diagonal
    mx_a = Matrix.create()
    mx_output = Matrix(mx_a.cols, mx_a.rows, [])

    for i in range(mx_output.rows):
        mx_output.matrix.append([])

    for col in range(mx_a.cols):
        for row in range(mx_a.rows):
            mx_output.matrix[col].append(mx_a.matrix[mx_a.rows - row - 1][mx_a.cols - col - 1])

    mx_output.print()


def transpose_vertical():
    # Transpose a matrix along it's vertical axis
    mx_a = Matrix.create()
    mx_output = Matrix(mx_a.rows, mx_a.cols, [])

    for row in range(mx_output.rows):
        mx_output.matrix.append([])
        for col in range(mx_output.cols):
            mx_output.matrix[row].append(mx_a.matrix[row][mx_a.cols - col - 1])

    mx_output.print()


def transpose_horizontal():
    # Transpose a matrix along a horizontal axis
    mx_a = Matrix.create()
    mx_output = Matrix(mx_a.rows, mx_a.cols, [])

    for row in range(mx_output.rows):
        mx_output.matrix.append([])
        for col in range(mx_output.cols):
            mx_output.matrix[row].append(mx_a.matrix[mx_a.rows - row - 1][col])

    mx_output.print()


def determinant_choice():
    mx_a = Matrix.create()
    while mx_a.rows != mx_a.cols:
        print('Rows and columns must be equal')
        mx_a = Matrix.create()
    print(calc_determinant(mx_a))


def calc_determinant(mx_a):
    # Calculates determinant of a matrix in a recursive manner
    if mx_a.rows == 1:
        return mx_a.matrix[0][0]
    # base case
    if mx_a.rows == 2:
        # calculate determinant of 2 x 2 matrix with element * (ad - bc)
        return (mx_a.matrix[0][0] * mx_a.matrix[1][1]) - (mx_a.matrix[0][1] * mx_a.matrix[1][0])

    return sum([(mx_a.matrix[0][x] * calc_determinant(Matrix(mx_a.rows - 1, mx_a.cols - 1, sub_matrix(mx_a, 0, x)))) * pow(-1, x) for x in range(mx_a.rows)])


def sub_matrix(mx_a, i, j):
    # Creates a submatrix by slicing an unwanted row i and unwanted col j
    sub_matrix = []
    for index, row in enumerate((mx_a.matrix[:i] + mx_a.matrix[i+1:])):
        sub_matrix.append([])
        sub_matrix[index] = row[:j] + row[j+1:]

    return sub_matrix


def matrix_inverse():
    mx_a = Matrix.create()
    # inverse is 1 / determinant x transposed (main diagonal) cofactors of all elements
    # cofactors are the determinants of each element in the matrix multiplied by -1 ^ (i+j)

    mx_a_det = calc_determinant(mx_a)

    if mx_a_det != 0:
        # create cofactor matrix
        mx_co = Matrix(mx_a.rows, mx_a.cols, [])
        for i in range(mx_co.rows):
            mx_co.matrix.append([])
            for j in range(mx_co.cols):
                mx_co.matrix[i].append(pow(-1, (i + j)) * calc_determinant(Matrix(mx_co.rows - 1, mx_co.cols - 1, sub_matrix(mx_a, i, j))))

        # transpose cofactor matrix along main diagonal
        mx_trsp = Matrix(mx_a.rows, mx_a.cols, [])
        for i in range(mx_trsp.rows):
            mx_trsp.matrix.append([])

        for col in range(mx_trsp.cols):
            for row in range(mx_trsp.rows):
                mx_trsp.matrix[col].append(mx_co.matrix[row][col])

        # calculate inverse of the determinant of original matrix
        inv_det = 1 / mx_a_det

        # multiply transposed cofactor matrix by inverted determinant
        mx_output = Matrix(mx_a.rows, mx_a.cols, [])

        for row in range(mx_output.rows):
            mx_output.matrix.append([])
            for col in range(mx_output.cols):
                mx_output.matrix[row].append(str(round(float(mx_trsp.matrix[row][col]) * inv_det, 4)))

        mx_output.print()
    else:
        print('No inverse exists because the determinant equals zero')


if __name__ == '__main__':
    while True:
        # ask for user input to choose an option
        print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose Matrix')
        print('5. Calculate determinant\n6. Calculate inverse\n0. Exit')
        choice = int(input('Your choice: '))

        if choice == 1:
            matrix_add()
        elif choice == 2:
            matrix_by_constant()
        elif choice == 3:
            matrix_by_matrix()
        elif choice == 4:
            matrix_transpose()
        elif choice == 5:
            determinant_choice()
        elif choice == 6:
            matrix_inverse()
        elif choice == 0:
            break
        else:
            print('Invalid choice, please try again')


