"""
1) Assume Python doesn’t implement “\b”. Write a regex expression that
implements “\b”. Also write the unit tests to verify your code.
"""

import re
import unittest


class TestBackslash(unittest.TestCase):

    def test_string_without_backslash(self):
        str = r"Mohamed Mahmoud Abdallah"
        expected_output = "Mohamed Mahmoud Abdallah"
        self.assertEqual(execute_backslash(str), expected_output)

    def test_string_with_one_backslash(self):
        str = r"Mohamed \bMahmoud Abdallah"
        expected_output = "MohamedMahmoud Abdallah"
        self.assertEqual(execute_backslash(str), expected_output)

    def test_string_with_two_backslashes(self):
        str = r"Mohamed \bMahmoud \bAbdallah"
        expected_output = "MohamedMahmoudAbdallah"
        self.assertEqual(execute_backslash(str), expected_output)


def execute_backslash(input_str):
    """
    This method accepts a string, check if it contains a backslash and if so it executes the
    backslash and returns the new string.
    """
    p = re.compile(r'\\b')
    output_list = p.split(input_str)
    if len(output_list) > 1:
        # There were a backslash in the input string
        output_str = ""
        for item in output_list[:-1]:
            output_str += item[:-1]  # remove the last charcter for executing backslash.
        output_str += output_list[-1]  # add last item from the output_list.
    else:
        # input string doesn't contain a backslash character
        output_str = input_str
    return output_str


def do_backslash():
    """
    Implement backslash behaviour.
    """
    input_str = raw_input("Please enter a raw string to check for backslashes : ")
    output_str = execute_backslash(input_str)

    print "Your string after executing backslash is: %s" % output_str


if __name__ == "__main__":
    do_backslash()
