
''' TODO: implement memory and allow overwriting with new matrix as function '''

class Matrix:

    def __init__(self, rows, cols, matrix):
        self.rows = int(rows)
        self.cols = int(cols)
        self.matrix = matrix
        self.dimensions = self.rows, self.cols
        if not self.matrix:
            for row in range(self.rows):
                self.matrix.append([])
                for col in range(self.cols):
                    self.matrix[row].append(' ')

        # actual matrix is a list of lists:
        # [[1,2,3],
        #  [1,2,3],
        #  [1,2,3]]


    def __repr__(self):
        # return Matrix(row, col, matrix)
        return f'Matrix({self.rows}, {self.cols}, {self.matrix})'

    def __str__(self):
        out = []
        for row in range(self.rows):
            out.append([])
            for col in range(self.cols):
                out[row].append(str(round(self.matrix[row][col], 2)))

        for row in range(self.rows):
             out[row] = ' '.join(map(str, out[row]))
        out = str('\n'.join(map(str, out)))

        return out

    def __add__(self,other):
        mx_output = Matrix(self.rows, self.cols, self.matrix)
        if isinstance(other, Matrix):
            if self.dimensions != other.dimensions:
                raise ValueError('Matrices must have the same dimensions. Please input again')
            for row in range(self.rows):
                for col in range(mx_output.cols):
                    mx_output.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
            return mx_output
        else:
            raise TypeError(f"Matrix objects do not support addition with {type(other)} objects")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError('The number of columns in matrix 1 must equal the rows of matrix 2. Please input again')
            mx_output = Matrix(self.rows, other.cols, [])
            for row in range(mx_output.rows):
                for col in range(mx_output.cols):
                    ele_sum = 0
                    for i in range(self.cols):
                        ele_sum += self.matrix[row][i] * other.matrix[i][col]
                    mx_output.matrix[row][col] = ele_sum
            return mx_output

        elif isinstance(other, float) or isinstance(other, int):
            mx_output = Matrix(self.rows, self.cols, self.matrix)
            for row in range(mx_output.rows):
                for col in range(mx_output.cols):
                    mx_output.matrix[row][col] = (self.matrix[row][col] * other)
            return mx_output
        else:
            raise TypeError(f'Matrix objects do not support multiplication with {type(other)} objects')

    @classmethod
    def create(cls):
        # input matrix dimensions (rows then cols)
        # input format is 'row col'
        rows, cols = [int(ele) for ele in input('Enter rows and columns of matrix: ').split()]
        mx = []
        # input matrix row by row with a space between each element
        print('Enter matrix row. Please leave a space between each element:')
        for i in range(rows):
            mx.append([])
            mx[i] = [float(ele) for ele in input().split()]
        return cls(rows, cols, mx)

    def transpose_main(self):
        # Transpose a matrix along it's main diagonal
        mx_output = Matrix(self.cols, self.rows, [])
        for col in range(mx_a.cols):
            for row in range(mx_a.rows):
                mx_output.matrix[col][row] = self.matrix[row][col]
        return mx_output

    def transpose_side(self):
        # Transpose a matrix along it's side diagonal
        mx_output = Matrix(self.cols, self.rows, [])
        for col in range(self.cols):
            for row in range(self.rows):
                mx_output.matrix[col][row] = self.matrix[self.rows - row - 1][self.cols - col - 1]
        return mx_output

    def transpose_vertical(self):
        # Transpose a matrix along it's vertical axis
        mx_output = Matrix(self.rows, self.cols, [])
        for row in range(mx_output.rows):
            for col in range(mx_output.cols):
                mx_output.matrix[row][col] = self.matrix[row][self.cols - col - 1]
        return mx_output

    def transpose_horizontal(self):
        # Transpose a matrix along a horizontal axis
        mx_output = Matrix(self.rows, self.cols, [])
        for row in range(mx_output.rows):
            for col in range(mx_output.cols):
                mx_output.matrix[row][col] = self.matrix[self.rows - row - 1][col]
        return mx_output

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError('The rows and columns must be equal to find the determinant')
        # Calculates determinant of a matrix in a recursive manner
        if self.rows == 1:
            return self.matrix[0][0]
        # base case
        if self.rows == 2:
            # calculate determinant of 2 x 2 matrix with element * (ad - bc)
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        # recursion statement
        return sum([(self.matrix[0][x] *
                     Matrix.determinant(Matrix(self.rows - 1, self.cols - 1, Matrix.sub_matrix(self, 0, x))))
                    * pow(-1, x)
                    for x in range(self.rows)])

    @staticmethod
    def sub_matrix(mx, i, j):
        # Creates a submatrix by slicing an unwanted row i and unwanted col j
        sub_matrix = []
        for index, row in enumerate((mx.matrix[:i] + mx.matrix[i + 1:])):
            sub_matrix.append([])
            sub_matrix[index] = row[:j] + row[j + 1:]
        return sub_matrix

    def invert(self):
        # inverse is 1 / determinant x transposed (main diagonal) cofactors of all elements
        # cofactors are the determinants of each element in the matrix multiplied by -1 ^ (i+j)
        mx_det = Matrix.determinant(self)
        if mx_det != 0:
            mx_output = Matrix(self.rows, self.cols, [])
            # create cofactor matrix
            for i in range(mx_output.rows):
                for j in range(mx_output.cols):
                    mx_output.matrix[i][j] = (pow(-1, (i + j)) * Matrix.determinant(
                        Matrix(mx_output.rows - 1, mx_output.cols - 1, Matrix.sub_matrix(self, i, j))))
            # transpose cofactor matrix along main diagonal
            mx_output.transpose_main()
            # calculate inverse of the determinant of original matrix
            inv_det = 1 / mx_det
            # multiply transposed cofactor matrix by inverted determinant
            mx_output = mx_output * inv_det
            return mx_output
        else:
            raise ValueError('No inverse exists because the determinant equals zero')


if __name__ == '__main__':
    print('Please input a matrix')
    mx_a = Matrix.create()
    while True:
        # print out matrix in memory
        # input a new matrix
        # ask for user input to choose an option
        print('Which operation would you like to carry out?\n'
              '1. Add matrices\n2. Multiply matrix by a constant\n'
              '3. Multiply matrices\n4. Transpose Matrix\n'
              '5. Calculate determinant\n6. Calculate inverse\n'
              '0. Exit')
        choice = int(input('Your choice: '))
        if choice == 1:
            print('Please input a second matrix')
            mx_b = Matrix.create()
            print(mx_a + mx_b)
            # keep in mem? y : mx_a = mx_a + mx_b
        elif choice == 2:
            num = int(input('Please input a constant: '))
            print(mx_a * num)
            # keep in mem? y : mx_a = mx_a * num
        elif choice == 3:
            print('Please input a second matrix')
            mx_b = Matrix.create()
            print(mx_a * mx_b)
            # keep in mem? y : mx_a = mx_a * mx_b
        elif choice == 4:
            while True:
                print('1. Main diagonal \n2. Side diagonal \n3. Vertical line \n4. Horizontal line \n'
                      '0. Exit to previous menu')
                transpose_choice = int(input('Your choice: '))
                if transpose_choice == 1:
                    print(mx_a.transpose_main())
                elif transpose_choice == 2:
                    print(mx_a.transpose_side())
                elif transpose_choice == 3:
                    print(mx_a.transpose_vertical())
                elif transpose_choice == 4:
                    print(mx_a.transpose_horizontal())
                elif transpose_choice == 0:
                    break
                else:
                    print('Invalid choice, please try again')
        elif choice == 5:
            print(mx_a.determinant())
        elif choice == 6:
            print(mx_a.invert())
        elif choice == 0:
            break
        else:
            print('Invalid choice, please try again')


