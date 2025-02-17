#Ledes Franc Ajuonoma
#17/02/25
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder



#define the funciton header called divisors expecting one argument

def divisors(num):        

    #set up an empty list to hold your result
    result = []
    
    #loop i from 1 to the number you are checking (take care not to include the number itself)
    for i in range(1,num):
        
        #if the remainder when dividing the number by i is equal to zero then i is a divisor so...
        if num % i == 0:

            #apend i to the list you set up
            
            result.append(i)
 
    #return the list

    return result
#to test the divisors function uncomment the following line it should give [1,2,3,5,6,10,15]
print(divisors(30))
