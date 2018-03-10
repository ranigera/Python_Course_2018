#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1
Student: Shiran Gera
ID: 039270624
"""
# 1)
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    is_match = False
    for i in range(len(word)-5):
        six_letters = word[i:i+6]
        if six_letters[0:5:2] == six_letters[1:6:2]:
            is_match = True
    return is_match
     
# Mock data (for example):    
word = 'fdsfdffrrvvdsz'
# Run the function:           
trifeca(word)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   

# 2)
def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
   """
   for i in range(100000,1000000):
       if str(i)[2:4] == str(i)[5:3:-1] \
       and str(i+1)[1:3] == str(i+1)[5:3:-1] \
       and str(i+2)[1:3] == str(i+2)[4:2:-1] \
       and str(i+3)[:3] == str(i+3)[5:2:-1]:
           print(i)

# Run the function:           
check_palindrome()    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -      

# 3)
def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    prefered_subject = {}
    for name in subj1_all_students:
        sub1_highest_score = max(subj1_all_students.get(name))
        sub2_highest_score = max(subj2_all_students.get(name,'No Score'))
        if type(sub2_highest_score) != str:
            if sub1_highest_score > sub2_highest_score:
                prefered_subject[name] = 'SUBJECT A'
            else:
                prefered_subject[name] = 'SUBJECT B'
    for name in prefered_subject:
        print(name, prefered_subject[name])

# Mock data (for example):
subj1_all_students={'Yosi':[20,30],'Dani':[40,90],'Tamar':[75,95], 'Dana':[60,85], 'Ziv':[43,73], 'Hadas':[99,43]}
subj2_all_students={'Yosi':[40,70],'Dani':[30,80],'Tamar':[90,40], 'Dana':[95,85], 'Gil':[79,60]}

# Run the function:           
compare_subjects_within_student(subj1_all_students, subj2_all_students)