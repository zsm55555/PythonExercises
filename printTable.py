# This program is taken from Automate The Boring Stuff With Python by: Al Sweigart
# Chapter 6 - Practice Problem - Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidths = [0] * len(list)
    # creates 3 lists based on the list length
    for row in range(len(list[0])):
        for col in range(len(list)):
            colWidths[col] = len((max(list[col], key=len)))
            # sets the column width to the maximum length of an item in the list
            print(list[col][row].rjust(colWidths[col]), end=' ')
        print()

printTable(tableData)
