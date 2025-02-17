#Ledes Franc Ajuonoma
#17/02/25
#perfectNumber.py

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

from divisors import divisors


#define the function header called perfectNumber expecting one argument
def perfectNumber(x):


    #set a result variable to False by default
    result = False


    #if the sum of all the divisors of the number is equal to the test number
    if result == x:

        #set the result variable to be True
         result = True

    #return the result variable
    return result


#uncomment the following line to test the perfectNumber function it should return True
if (perfectNumber(8128)): print("8128 is a perfect number")

