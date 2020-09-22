"""
Morgan Christensen

Module 3 - average scores

09/20/20
"""


def average() :
    test1 = input("Enter test 1 score: ")
    test2 = input("Enter test 2 score: ")
    test3 = input("Enter test 3 score: ")
    average_score = (int(test1) + int(test2) + int(test3))/3
    return average_score


if __name__ == '__main__':
    lastName = input("Enter your last name: ")
    firstName = input("Enter your first name: ")
    age = input("Enter your age: ")
    average_scores = average()
    print("{}, {} age: {} Average grade: {}".format(lastName, firstName, age, average_scores))