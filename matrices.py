""" 
Matrices.py
This program assumes a square matrix as input of form (a,b,c);(d,e,f);(g,h,i)
After input, the user is asked what operations should be done to it.
Operations that are within the scope of this program to return are:
Row reduction, transposition, inversion, determinant, eigenvalues, eigenvectors(?).

Make your Declarations!
"""
import math

# Function to convert input string to lists of numbers
def myAtoI( string ):
    string = string.replace('(','')
    string = string.replace(')','')
    given_row = [float(string.split(',')[i]) for i in range(len(string) - string.count(","))]
    return given_row

# Function to take in and make a matrix
def matrix_input( ):
    global matrix
    input_string = input("Please input the matrix in the fashion of (a,b);(c,d): ")
    matrix = [myAtoI(row) for row in input_string.split(';')]
    print(matrix)
    return 0

# Row Reduces the input matrix
def rref(matrix_given):
    rref_matrix = [[c for c in matrix_given[i]] for i in range(len(matrix_given))]
    print(rref_matrix)
    leading_one = 0
    rowCount = len(rref_matrix)
    columnCount = len(rref_matrix[0])
    for row in range(rowCount):
        if columnCount <= leading_one:
            break
        r = row
        while rref_matrix[r][leading_one] == 0:
            r += 1
            if rowCount == r:
                r = row
                leading_one += 1
                if columnCount == leading_one:
                    return rref_matrix
        rref_matrix[r], rref_matrix[row] = rref_matrix[row], rref_matrix[r]
        if rref_matrix[row][leading_one] != 0:
            rref_matrix[row][:] = [x / rref_matrix[row][leading_one] for x in rref_matrix[row]]
        for new_row in range(len(rref_matrix)):
            if new_row != row:
                rref_matrix[new_row][:] = [x - (rref_matrix[new_row][leading_one] * rref_matrix[row][rref_matrix[new_row].index(x)]) for x in rref_matrix[new_row]] 
        leading_one += 1
        print(rref_matrix)
    return rref_matrix

# Finds Image and Kernel of input matrix
def im_and_ker():
    image_span = []
    # Make columns of RREF rows to access easier
    rref_transposed = list(zip(*rref(matrix)))
    # Find the columns of RREF that have leading ones
    for index, row in enumerate(rref_transposed):
        # Note leading one should be indexed same as row
        if row.count(0) == (len(row) - 1) and row.index(1) == index:
            # Image spans the pivot columns of original matrix
            image_span.append(list(zip(*matrix))[index])
        else:
            # Kernel spans the columns of rref without leading ones
            kernel_span = [-c for c in row]
            kernel_span[index] += 1

    print("Image spans the columns: ", image_span)
    print("Kernel basis spans the columns: ", kernel_span)

    return 0
    
# Returns transpose of matrix
def transpose( ):
    print(list(zip(*matrix)))
    return 0

# Returns next matrix of laplace expansion
def laplace(given_matrix, given_column, given_row):
    return [[given_matrix[row][c] for c in range(len(given_matrix[row])) if c != given_column] for row in range(len(given_matrix)) if row != given_row]
    

# Finds determinant of input matrix
def determinant(given_matrix):
    # Laplace Expansion and Recursion are better
    # base case, 2x2
    if len(given_matrix) == 2:
        return ((given_matrix[0][0]*given_matrix[1][1]) - (given_matrix[0][1]*given_matrix[1][0]))
    else:
        # Check for row / column with most 0s
        
        # Check for square matrix in case
        if len(given_matrix) == len(given_matrix[0]):
            # Check rows
            start_column = 0
            start_row = 0
            column_zeroes = 0
            row_zeroes = 0
            for row in given_matrix:
                # Check for row of mostly 0s
                if row.count(0) > row_zeroes:
                    row_zeroes = row.count(0)
                    start_row = given_matrix.index(row)
            # Transpose and check columns
            transposed = list(zip(*given_matrix))
            for column in transposed:    
                if column.count(0) > column_zeroes:
                    column_zeroes = column.count(0)
                    start_column = transposed.index(column)
            start = True if row_zeroes > column_zeroes else False

            # Make a matrix that will tell us the sign
            sign_matrix = [[math.pow(-1, (c + given_matrix.index(row))) for c in range(len(row))] for row in given_matrix]
            # Now recursively find determinant
            d = 0
            if start:
                for c in given_matrix[start_row]:
                    if c != 0:
                        d += (sign_matrix[start_row][given_matrix[start_row].index(c)] * c) * determinant(laplace(given_matrix, given_matrix[start_row].index(c), start_row))
                return d
            else:
                for c in transposed[start_column]:
                    if c != 0:
                        d += (list(zip(*sign_matrix))[start_column][transposed[start_column].index(c)] * c) * determinant(laplace(transposed, transposed[start_column].index(c), start_column))
                return d


        # Not Square
        else:
            print("Not possible for rectangle matrix.")
            return 0

# Finds the inverse matrix
def inverse():
    return 0

# Finds eigenvalues
def eigenvalues():
    return 0

# Finds eigenvectors
def eigenvectors():
    return 0

def testers( ):
    return 0    

# Main menu function
def post_input():
    while True:
        print("""What would you like us to do with your matrix?
        1. Find Row Reduced Echelon Form
        2. Find the Image and Kernel
        3. Find the Transpose
        4. Find the Determinant
        5. Find the Inverse (if invertible)
        6. Find the Eigenvalues
        7. Find the Eigenvectors
        8. Enter a New Matrix
        9. Exit""")
        ans = input(": ")
        if ans == "9":
            print("\nGoodbye.\n")
            exit()
        elif ans == "1":
            print("RREF is: ", rref(matrix))
            post_input()
        elif ans == "2":
            im_and_ker()
            post_input()
        elif ans == "3":
            transpose()
            post_input()
        elif ans == "4":
            print("Determinant is: ", determinant(matrix))
            post_input()
        elif ans == "5":
            inverse()
            post_input()
        elif ans == "6":
            eigenvalues()
            post_input()
        elif ans == "7":
            eigenvectors()
            post_input()
        elif ans == "8":
            matrix_input()
            post_input()
        else:
            print("Not a valid input.")
            post_input()

# Function for the start of the program
def start():
    while True:
        print("""
        1. Input a matrix
        2. Exit
        """)
        ans = input("What is your choice? ")
        if ans == "2":
            print("\nGoodbye.\n")
            return 0
        elif ans == "1":
            matrix_input()
            post_input()
        else:
            print("\n not a valid response")

if __name__ == "__main__":
    start()
