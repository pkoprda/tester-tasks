#!/usr/bin/python3.9
# coding=utf-8

# Task 1 - Palindrome

from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(description="Palindrome tester")
    parser.add_argument('text', metavar='TEXT', help='string that will be tested')
    return parser.parse_args()

def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    text = parse_arguments().text
    if is_palindrome(text):
        print(f"String '{text}' is a palindrome")
    else:
        print(f"String '{text}' is not a palindrome")
