"""
----------------------------------------------------
asgn.py
Holds functions for assignment 8.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-16"
----------------------------------------------------
"""
from letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects 
            to retrieve data from (BST)
    Postconditions:
        Each Letter object in bst contains the number of comparisons
        found by searching for that Letter object in file_variable.
    -------------------------------------------------------
    """
    file_variable.seek(0)
    line = file_variable.readline()
    while line != "":
        for letter in line:
            if letter != " " and letter.isalpha():
                letter_obj = Letter(letter.upper())
                value = bst.retrieve(letter_obj)
        line = file_variable.readline()

    return

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    -------------------------------------------------------
    Preconditions:
        bst - a binary search tree of Letter objects (BST)
    Postconditions:
        returns
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    l = bst.inorder()
    for letter in l:
        total += letter.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts.
    -------------------------------------------------------
    Preconditions:
        bst - a binary search tree of Letter objects (BST)
    Postconditions:
        Prints a table of letter counts for each Letter object
        in bst
    -------------------------------------------------------
    """
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    l = bst.inorder()
    for letter in l:
        total += letter.count
    
    print("Letter Count/Percent Table")
    print("")
    print("Total Count: {}".format(total))
    print("")
    print("Letter  Count       %")
    print("---------------------")
    if total > 0:
        for letter in l:
            percentage = letter.count / total * 100
            print("{:>5}   {:<6}  {:<.2f}%".format(letter.letter, letter.count, percentage))     
    else:
        print("No letters found.")
    return
