"""
2) [20 points] Write a program (starting from 'using') that gets a keyword from
the user and then also gets a phrase. The program should then output the number
of times that the keyword appeared in their phrase, repeating their keyword in
quotes. The program should perform a search is case-insensitive and a casesensitive
search. The program will NOT count partial word matches, 'the' should
NOT match against 'them' or 'their'. A sample run is shown below:
Enter a keyword: the
Enter a phrase: The lord of the rings is their best movie!
Case-sensitive search: The keyword 'the' appeared 1 times in your phrase.
Case-insensitive search: The keyword 'the' appeared 2 times in your phrase.
Enter a keyword: THE
Enter a phrase: The lord of the rings is their best movie!
Case-sensitive search: The keyword 'THE' appeared 0 times in your phrase.
Case-insensitive search: The keyword 'THE' appeared 2 times in your phrase.
"""


def count_keyword_in_phrase(keyword, phrase):
    word_list = phrase.split(" ")
    occurness_cs = word_list.count(keyword)
    word_list = phrase.lower().split(" ")
    occurness_cis = word_list.count(keyword.lower())
    return occurness_cs, occurness_cis


def read_validate_user_input():
    keyword = raw_input("Enter a keyword: ")
    phrase = raw_input("Enter a phrase: ")
    #TODO: add input validation
    return keyword, phrase


if __name__ == "__main__":
    keyword, phrase = read_validate_user_input()
    occurness_cs, occurness_cis = count_keyword_in_phrase(keyword, phrase)
    print 'Case-sensitive search: The keyword "%s" appeared %s times in your phrase.' % (keyword,
                                                                                         occurness_cs)
    print 'Case-insensitive search: The keyword "%s" appeared %s times in your phrase.' % (keyword,
                                                                                           occurness_cis)
