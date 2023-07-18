det = 0                                                                                 ## variable for holding variable
x = 1
#determinant function
#--------------------------------------------------------------------------------------------------------------------#

def determinant(arr):

    row = list(range(len(arr)))                                                 ##for the indexes of the row

    if ( len(arr) == 2 ) and len(arr[0]) == 2:                            ##when the order of the matrix is 2x2
        inner_d = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0] ##basic determinant formula
        print(inner_d)                                                             ## printing the value of solved determinants
        global x
        x += 1
        return inner_d                                                              ## this value will be stored in the variable(inner_det)
                                                                                                
    for ind in row:                                                                 ## for values of rows
        print(x," ; ind == 0", ind, sep = "")
        arr_b = arr.copy()                                                        ## copy the matrix
        arr_b = arr_b[1:]                                                           ##remove first row of copied index
 
        for i in range(len(arr_b)):                                             ## for the values of associated  columns
            arr_b[i] = arr_b[i][0:ind] + arr_b[i][ind+1:]           ## stitches the columns adjacent to the associated columns
 
        sign = (-1) ** (ind % 2)                                                ## for the sign (-1)^odd/even number
        inner_det = determinant(arr_b)                                  ## calls the function again, holds the value of inner_d
        
        global det                                                                      ## declaring det as global
        det += sign * arr[0][ind] * inner_det                           ## adds subsequent valyues of determinants
        
    return det                                                                          ## function returns the value of determinant, when no more 2x2
                                                                                                ## are left

#printing fuction
#--------------------------------------------------------------------------------------------------------------------#

def show():                                                                         ## function for printing the matrix
    print()
    for j in range(len(arr)):                                                   ## prints each row one by one
        print(arr[j])
    print()

#value assign function
#--------------------------------------------------------------------------------------------------------------------#

def assign():                                                                       ## function for assigning values to rows
    for i in range (n):                                                             ## n == order of matrix
        print("enter the values for row",i+1,"seperated by commas")
        
        while True:                                                                 ## block to check if number of entries is equal to the order
            x = list(eval(input("")))
            if len(x)== n:
                break
            else:
                print("please enter",n,"values (seperated by commas) ")
    
        arr.append(x)                                                               ## appending each row to the matrix
    show()                                                                              ## calls the function to print

#program
#--------------------------------------------------------------------------------------------------------------------#

n = int(input("enter order of matrix \n"))
arr = []
assign()
print(determinant(arr))                                                 ## calling the function inside print(), prints det
#--------------------------------------------------------------------------------------------------------------------#
