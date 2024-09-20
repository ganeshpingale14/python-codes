a="Here are some problem statements covering the topics of if-else, for/while loops, list, and tuple in Python:1. If-Else ProblemsOdd or Even: Write a program that takes an integer input from the user and prints whether the number is odd or even.Leap Year Checker: Write a program to check if a year entered by the user is a leap year or not.Largest of Three Numbers: Write a program to find the largest of three numbers entered by the user."

import time
import sys
def animation_text(text):
    for i in text:
        print(i,end="")
        time.sleep(0.02)
        sys.stdout.flush()

animation_text(a)