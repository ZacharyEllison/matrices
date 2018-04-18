""" 
Matrices.py
This program assumes a square matrix as input of form (a,b,c);(d,e,f);(g,h,i)
After input, the user is asked what operations should be done to it.
Operations that are within the scope of this program to return are:
Row reduction, transposition, inversion, determinant, eigenvalues, eigenvectors(?).

Make your Declarations!
"""

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
    rref_transposed = list(zip(*rref(matrix)))
    for index, row in enumerate(rref_transposed):
        if row.count(0) == (len(row) - 1):
            image_span.append(list(zip(*matrix))[index])
    print("Image spans the columns: ", image_span)
    
    ker = []

    return 0
    
# Returns transpose of matrix
def transpose( ):
    print(list(zip(*matrix)))
    return 0

# Finds determinant of input matrix
def determinant():
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
            determinant()
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
