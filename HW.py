# 1
salary = int(input("Enter beginning salary : "))
change = 1
for i in range(4):
    change *= 1.05

salary *= change

print("New salary: ${:,.2}".format(salary))
print("Change: {:.2%}".format(change - 1))

# 2
first_set = set(eval(input("Enter the first set: ")))
second_set = set(eval(input("Enter the second set: ")))

jaccard_similarity_coefficient = len(first_set.intersection(second_set)) / len(first_set.union(second_set))
print("the Jaccard similarity coefficient is {:.3f}".format(jaccard_similarity_coefficient))

# 3
# find, index 사용 , for문 (발견하고 break)
sentence = input("Enter a sentence")
word1 = input("Enter word to replace")
word2 = input("Enter replacement word")
sentence.find(word1)
# 4
# sorted x (sort method)
# 짝홀수 if문으로 나누기

# 5
characters = input("Enter the sequence of characters: ")

for char in characters:
    if char.isalpha():
        new_characters += char.lower()

print(new_characters)
######################방법1####################
characters = input("Enter the sequence of characters: ")

new_characters = "".join(char.lower() if char.isalpah() else "" for char in characters)

reversed_characters = "".join(reversed(new_characters))

if new_characters == reversed_characters:
    print("{} is Palindrome.".format(characters))
else:
    print("{} is not Palindrome.".format(characters))


#####################방법2(재귀)################
def main():
    characters = input("Enter the sequence of characters: ")

    new_characters = "".join(char.lower() if char.isalpah() else "" for char in characters)

    if isPalindrome(new_characters):
        print("{} is Palindrome.".format(characters))
    else:
        print("{} is not Palindrome.".format(characters))


def isPalindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False


main()


# 6
# skeleton code 써서 빈칸 채우기
# 0팩 =1 , 1팩=1 , 2팩=2
# if문은 0이면  안됨, 1또는 2인경우 체크
# n!= n(n-1)

# 7
def main():
    list_of_number = eval(input("Enter the numbers: "))
    list_of_number.sort(key=sum_of_digits)
    print("the sorting result is {}".format(str(list_of_number)))


def sum_of_digits(number):
    # the return value of this function should be comparable.
    # hint: (10, 7) > (10, 5) is True
    sum_digits = 0
    for i in str(number):
        sum_digits += int(i)
    return sum_digits, number


main()


##7
def main():
    list_of_number = eval(input("Enter the numbers: "))
    list_of_number.sort(key=sum_of_digits)
    print("the sorting result is {}".format(str(list_of_number)))


def sum_of_digits(number):
    sum_digits = sum(map(int, strt(number)))

    return sum_digits, number


main()

# 8
import math

a = [1, 2, 3, 4, 5]

print(math.sqrt(a))



