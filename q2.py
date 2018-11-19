"""
----------------------------------------------------
q2.py
Comparison count for bst.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-15"
----------------------------------------------------
"""
from bst_linked import BST
from letter import Letter
from asgn08 import comparison_total, do_comparisons

def fill_letter_bst(bst, data):
    for i in data:
        letter = Letter(i)
        bst.insert(letter)
    return

bst1 = BST()
bst2 = BST()
bst3 = BST()

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

fill_letter_bst(bst1, DATA1)
fill_letter_bst(bst2, DATA2)
fill_letter_bst(bst3, DATA3)

file_variable = open('gibbon.txt', 'r')

do_comparisons(file_variable, bst1)
do_comparisons(file_variable, bst2)
do_comparisons(file_variable, bst3)
 
total1 = comparison_total(bst1)
total2 = comparison_total(bst2)
total3 = comparison_total(bst3)
 
print("Data1",total1)
print("Data2",total2)
print("Data3",total3)