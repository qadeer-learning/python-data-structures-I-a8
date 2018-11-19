"""
----------------------------------------------------
q3.py
Prints letter table
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-16"
----------------------------------------------------
"""
from asgn08 import letter_table, do_comparisons
from bst_linked import BST
from letter import Letter

data = "ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst = BST()

def fill_letter_bst(bst, data):
    for i in data:
        letter = Letter(i)
        bst.insert(letter)
    return

fill_letter_bst(bst, data)
file_variable = open('gibbon.txt', 'r')
do_comparisons(file_variable, bst)

letter_table(bst)