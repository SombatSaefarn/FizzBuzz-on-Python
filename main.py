#making a function called FizzBuzz
def FizzBuzz(
    #starting range variable
    start: int,
    #ending range variable
    end: int,)-> None: #specifying that this function will return None
    print(start)
    #starting for loop starting with the variable start and end with end variable and assign variable called i
    for i in range(
            #starting range variable
            start,
            #ending range variable + 1
            end+1,
            ):
        #if i variable is dividable by 3 and 5 without leaving no remainders
        if i % 3 == 0 and i % 5 == 0:
            #printing "i FizzBuzz" if the condition is True
            print(f"{i} FizzBuzz")
        #else if i is dividable by 3 without leaving no remainders
        elif i % 3 == 0:
            #print "i Fizz" if the codition is True
            print(f"{i} Fizz")
        #else if i is dividable by 5 without leaving no remainders
        elif i % 5 == 0:
            #print "i Buzz" if the codition is True
            print(f"{i} Buzz")
        #else
        else:
            #print i if the no conditions are True
            print(f"{i}")
#calling the function FizzBuzz and has 1 as start arguement, 100 as end arguement
FizzBuzz(1,100)
