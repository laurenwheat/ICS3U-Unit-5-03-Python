#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program determines the factorial of a number


def grade_level(grade):

    if grade == "4+":
        grade_percent = 97
        return grade_percent
    elif grade == "4":
        grade_percent = 90
        return grade_percent
    elif grade == "4-":
        grade_percent = 83
        return grade_percent
    elif grade == "3+":
        grade_percent = 78
        return grade_percent
    elif grade == "3":
        grade_percent = 75
        return grade_percent
    elif grade == "3-":
        grade_percent = 71
        return grade_percent
    elif grade == "2+":
        grade_percent = 68
        return grade_percent
    elif grade == "2":
        grade_percent = 65
        return grade_percent
    elif grade == "2-":
        grade_percent = 61
        return grade_percent
    elif grade == "1+":
        grade_percent = 58
        return grade_percent
    elif grade == "1":
        grade_percent = 55
        return grade_percent
    elif grade == "1-":
        grade_percent = 51
        return grade_percent
    elif grade == "R" or grade == "r":
        grade_percent = 25
        return grade_percent
    else:
        grade_percent = -1
        return grade_percent


def main():

    grade_input = input("Enter your grade level: ")

    grade_percentage = grade_level(grade_input)

    if grade_percentage == -1:
        print("That is not a real mark!!")
    else:
        print("{0} is equal to a {1} percent. Thanks for playing<3"
              .format(grade_input, grade_percentage))


if __name__ == "__main__":
    main()
