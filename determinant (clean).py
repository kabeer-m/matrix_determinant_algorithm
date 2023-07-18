while True:                         # main loop

    det = 0

    #determinant function
#--------------------------------------------------------------------------------------------------------------------#

    def determinant(arr):

        row = list(range(len(arr))) 

        if ( len(arr) == 2 ) and len(arr[0]) == 2:
            inner_d = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
            print(inner_d)
            print()
            return inner_d
        
        for ind in row:
            print("ind == 0", ind, sep = "")
            arr_b = arr.copy() 
            arr_b = arr_b[1:]  
     
            for i in range(len(arr_b)):
                arr_b[i] = arr_b[i][ 0:ind ] + arr_b[i][ ind+1 : ] 
            sign = (-1) ** (ind % 2) 
            inner_det = determinant(arr_b)
            
            global det
            det += sign * arr[0][ind] * inner_det
            i
            
        return det

    #printing fuction
#--------------------------------------------------------------------------------------------------------------------#

    def show():
        print()
        for j in range(len(arr)):
            print(arr[j])
        print()

    #value assign function
#--------------------------------------------------------------------------------------------------------------------#

    def assign():
        for i in range (n):
            print("enter the values for row",i+1,"seperated by commas")
            
            while True:
                x = list(eval(input("")))
                if len(x)== n:
                    break
                else:
                    print("please enter",n,"values (seperated by commas) ")
        
            arr.append(x)
        show()

    #program
#--------------------------------------------------------------------------------------------------------------------#

    n = int(input("enter order of matrix \n"))
    arr = []
    assign()

    print(determinant(arr))
#--------------------------------------------------------------------------------------------------------------------#
    again = input("again?")
    if again == "y":
        continue
    else:
        break
