##################################################################
#  Computer Project #4
#
# Program that has multiple mathematical equations n\
# to calculate the problem based on the option selected \n
#
# The first part of the program indicates the MENU options \n
#
# The next part has all the functions from the MENU \n
# options. This is where the calculations are made for \n
# each menu option
#
# The main function is where the user enters a while loop \n
# which prompts the user to enter an option from the MENU
#
# If the user enters a valid option, the program will \n
# run the code corresponding to that option
#
# If the user enters an invalid option, the program will \n
# print an error and prompt the user to enter a valid option
#
#
# The program will continue to run until the user selects \n
# option "X" or "x", which will then print "Thank you for playing" 
##################################################################
import math
EPSILON = 0.0000001 

# Menu options for the user
MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''
# This is where the calculations are made for each option(Besides M and X)
def factorial(N): 
    ''' Docstring ''' 
    if not(N.isdigit() and int(N) >= 0):
         return None
    if N == '0':
        return 1
    N_sum = 1
    for i in range(1,int(N)+1):
        N_sum = N_sum * i

    return N_sum

def e(): 
    ''' Docstring ''' 
    denominator = 1
    e_sum = 1

    while 1/math.factorial(denominator) > EPSILON:
        e_sum = e_sum + 1/math.factorial(denominator)
        denominator += 1

    return round(e_sum,10)

def pi():
    ''' Docstring ''' 
    n = 0
    n_sum = 0
    while abs((-1)**n/(2*n+1)) > EPSILON:
        n_sum = n_sum + (-1)**n/(2*n+1)
        n += 1   
    n_sum = n_sum * 4
    return round(n_sum,10)
def sinh(x): 
    ''' Docstring ''' 
    if float_check(x):
    
        n = 0.0
        n_sum = 0
        while abs((float(x)**(2*n+1))/(math.factorial((2*n+1)))) > EPSILON:
            n_sum = n_sum + float(x)**(2*n+1)/math.factorial((2*n+1))
            n += 1
        return round(n_sum,10)

    else:
        return None
#Float check that returns true or false based on the input
def float_check(n):
    n = str(n)
    char = "1234567890."
    decimal_count = 0
    for i in range (len(n)):
        if n[i] == "-":
            if i == 0:
                continue
            else:
                return True
        if (n[i] not in char):
            return False
        if(n[i] == '.'):
            decimal_count += 1
    if(decimal_count>1):
        return False
    return True
# The while loop where the program will prompt the user for an option.
# Based on the option given, the program will make the calculation \n
# needed for it
def main(): 
    print(MENU) 
    option = input("\nChoose an option: ")

    

    while option != "X" and option != "x":

        if option == "F" or option == "f":
            print("\nFactorial")

            select = input("Input non-negative integer N: ")
            if select.isdigit():
                select = int(select)
                if select < 0:
                    print("\nInvalid N.")
                else:
                    calculated = factorial(str(select))
                    print("\nCalculated:", calculated)
                    f = math.factorial(select)
                    print("Math:",round(f,))
                    diff = calculated - f
                    print("Diff:",diff)
                    
            else:
                print("\nInvalid N.")
            
            


        if option == "E" or option == "e":
            print("\ne") 

            calculated = e()
            print("Calculated:", calculated)
            f_e = round(math.e,10)
            print("Math:",f_e)
            diff = f_e - calculated
            print("Diff: {:.10f}".format(diff))
        

        if option == "P" or option == "p":
            print("\npi")
            
            pi_calc = pi()
            print("Calculated:", pi_calc)
            f_p = math.pi
            print("Math:",round(f_p,10))
            diff_p = f_p - pi_calc
            print("Diff: {:.10f}".format(diff_p))
        

        if option == "S" or option == "s":
            print("\nsinh")
            option_s = input("X in radians: ")

            try:
                option_s = float(option_s)
                
                s_calc = sinh(option_s)
                print("\nCalculated:", s_calc)
                f_s = math.sinh(float(option_s))
                print("Math:",round(f_s,10))
                diff_s = f_s - s_calc
                print("Diff: {:.10f}".format(diff_s))
        
            except:
                print("\nInvalid X.")
        if option == "M" or option == "m":
            print(MENU)
       
# If the user enters an invalid option, the program will print the invalid \n
# option
# The program will also print the MENU options and prompt the user to enter \n
# another option
        if option.upper() != "F" and option.upper() != "E" and option.upper() != "P" and option.upper() != "S" and option.upper() != "M":
            print("\nInvalid option:",option.upper())
            print(MENU)
        option = input("\nChoose an option: ")

# If the user selects option "X" or "x", the program will print a thank you \n
# message
    if option == "X" or option == "x":
        print("\nThank you for playing.")
            



    

 
    
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()
