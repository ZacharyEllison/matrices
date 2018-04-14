""" 
Matrices.py
This program assumes a square matrix as input of form (a,b,c);(d,e,f);(g,h,i)
After input, the user is asked what operations should be done to it.
Operations that are within the scope of this program to return are:
Row reduction, transposition, inversion, determinant, eigenvalues, eigenvectors(?).
"""

"""
How do you want to have the matrix input?

[[a,b,c],[d,e,f],[g,h,i]]
This way I know the row and column rather easily
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
def rref():
#    if rref_found != True:
    global rref_matrix
    rref_matrix = matrix
    row = 0
    for leading_one in range(len(rref_matrix)):
        lead = False
        while lead == False:
            if rref_matrix[row][leading_one] == 0: # can't be LO
                row += 1
            else:
                # Make this leading one the right row
                rref_matrix[row], rref_matrix[leading_one] = rref_matrix[leading_one], rref_matrix[row]
                # Divide the row to make leading one a one
                for column in range(len(matrix[leading_one])):
                    rref_matrix[leading_one][column] = rref_matrix[leading_one][column] / rref_matrix[leading_one][leading_one]
                    # While at it, subtract from all rows 
                    for new_row in range(len(rref_matrix)):
                        if new_row == leading_one:
                            pass
                        else:
                            if rref_matrix[new_row][column] != 0:
                                rref_matrix[new_row][column] -= rref_matrix[leading_one][column]
                            else:
                                pass
                lead = True
    print(rref_matrix)
    rref_found = True
    return 0
    # else:
    #     print(rref_matrix)
    #     return 0

# Finds Image and Kernel of input matrix
def im_and_ker():
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
        print("""
        What would you like us to do with your matrix?
        1. Find Row Reduced Echelon Form
        2. Find the Image and Kernel
        3. Find the Transpose
        4. Find the Determinant
        5. Find the Inverse (if invertible)
        6. Find the Eigenvalues
        7. Find the Eigenvectors
        8. Exit""")
        ans = input(": ")
        if ans == "8":
            print("\nGoodbye.\n")
            exit()
        elif ans == "1":
            rref()
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
