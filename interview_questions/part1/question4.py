"""
4) Write a program that prints the numbers from 1 to 100. But for multiples of
three print 'Fizz' instead of the number and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""


def check_multipliers_three_five(start, end):
    output = ""
    for i in range(start, end):
        if (i % 3 == 0) and (i % 5 == 0):
            output += "FizzBuzz "
        elif (i % 3 == 0):
            output += "Fizz "
        elif (i % 5 == 0):
            output += "Buzz "
        else:
            output += str(i) + " "
    return output

if __name__ == "__main__":
    output = check_multipliers_three_five(1, 101)
    print output
