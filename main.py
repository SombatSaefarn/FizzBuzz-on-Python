def FizzBuzz(start: int, end: int) -> None:
    '''
    FizzBuzz program.
    :param start:
    :param end:
    :return None:

    on the printing process
    print "i FizzBuzz" if i is divisable by 3 and 5
    print "i Fizz if" i is divisable by 3
    print "i Buzz if" i is divisable by 5
    '''
    
    for i in range(start, end + 1):
        print(i, end = " ")
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print()

FizzBuzz(1,20)
