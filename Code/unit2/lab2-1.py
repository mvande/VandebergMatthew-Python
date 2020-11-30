#Matthew Vandeberg
#Period 2 Intro to Python

def main():
    #Make an int and float then print the sum
    int1 = 1
    float1 = 6.3
    print(int1 + float1)

    #Make an int and float then print the sum as an int using typecasting
    int2 = 4
    float2 = 5.4
    print(int(int2 + float2))

    #Ask for a number input, cast it as an int, add the input to 5, 
    #typecast the sum as a string, and finally print "Results: <sum>"
    #A simplified version would be: print(5 + int(input("Enter a number: ")))
    print("Results: " 
          + str(int(input("Enter a number: ")) 
          + 5))

    #Assign values to a bunch of variables 
    i = 100
    j = 200
    x = 300
    y = 100

    #Print the results of a bunch of boolean operations
    print(i == j or i > x)
    print(i < j and i >= y)
    print(i != j and i != x)
    print(i < j and i < x and i < y)
main()