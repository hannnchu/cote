def main():
    number = int(input("Enter the number: "))
    factorial_of_number = factorial(number)
    print("The factorial if {} is {:,}".format(number,\
                                               factorial_of_number))

def factorial(number):
    if number > 1:
        return number*factorial(number-1)
    else:
        return number


main()

