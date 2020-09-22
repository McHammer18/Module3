"""
Morgan Christensen

Module 3 - average scores

09/20/20
"""


def average(test1, test2, test3):
    if test1 > 0 and test2 > 0 and test3 > 0:
        average_score = (int(test1) + int(test2) + int(test3)) / 3
    else:
        raise ValueError
    return round(average_score, 2)


if __name__ == '__main__':
    lastName = input("Enter your last name: ")
    firstName = input("Enter your first name: ")
    age = input("Enter your age: ")
    test1 = input("Enter test 1 score: ")
    test2 = input("Enter test 2 score: ")
    test3 = input("Enter test 3 score: ")
    try:
        average_scores = average(int(test1), int(test2), int(test3))
    except Exception:
        raise(ValueError)
        print("There was a problem finding the average score")
    print("{}, {} age: {} Average grade: {}".format(lastName, firstName, age, average_scores))
