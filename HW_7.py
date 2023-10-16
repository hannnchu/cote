def main():
    list_of_number = eval(input("Enter the numbers: "))
    list_of_number.sort(key=sum_of_digits)
    print("the sorting result is {}".format(str(list_of_number)))


def sum_of_digits(number):
    sum_digits = sum(map(int, str(number)))
    return sum_digits, number


main()
