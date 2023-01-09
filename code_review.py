#!/usr/bin/python3.9
# coding=utf-8

# Task 2

def foo1(items):
    result = []
    [result.append(item) for item in items if item not in result]
    return result
