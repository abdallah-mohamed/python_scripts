"""
1) [20 points] Write a program that repeatedly collects positive integers from
the user, stopping when the user enters a negative number or zero. After that,
output the product of all positive entries. A sample run should appear on the
screen like the text below:
Enter a number: 3
Enter a number: 10
Enter a number: 2
Enter a number: -213
The product of all your positive numbers is 60.
"""
import operator


def positive_numbers_multiplier():
    numbers_list = []
    num = int(raw_input("Enter a number: "))
    while num > 0:
        numbers_list.append(num)
        num = int(raw_input("Enter a number: "))

    print "The product of all your positive numbers is %s." % reduce(operator.mul,
                                                                     numbers_list, 1)


if __name__ == "__main__":
    positive_numbers_multiplier()
