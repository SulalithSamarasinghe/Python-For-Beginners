while True:
    try:
        number = float(input('Enter a number : '))
        print('')
        result = 12.0/number
        print('12.0/',number,' = ',result)
        break
    except ValueError:
        print('')
        print('ValueError occurred!')
        print('You have enterd a character string.')
        print('Please only enter numbers.')
        print('')
    except ZeroDivisionError:
        print('')
        print('ZeroDivisionError occurred!')
        print('You have divided the number by zero!')
        print('Please only enter numbers.')
        print('')
    except:
        print('')
        print('An unknown error occurred!')
        print('')
    finally:
        #This will always loop through
        print('')
        print('Loop is completed.')
        print('')
