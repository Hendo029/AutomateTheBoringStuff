tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
separator = ' '
useMaxWidth = False

def printTable(table):
    # find longest word in column
    colWidths = [0] * len(table)        # create list for storing widths for each column, also amount of columns
    for column in range(len(colWidths)):
        maxLen = 0
        # Get the max length for each column and add it to the list colWidths
        for row in range(len(table[column])):
            if len(table[column][row]) > maxLen:
                maxLen = len(table[column][row])
        colWidths[column] = maxLen

    # Justify each word to lenght of the longest word
    for i in range(len(table)):
        for k in range(len(table[i])):
            if not useMaxWidth:
                table[i][k] = table[i][k].rjust(colWidths[i])
            else:
                table[i][k] = table[i][k].rjust(max(colWidths))

    # making a list that contains lists with words in new order
    num_cols = len(table[0])
    rowNew = [[] for _ in range(num_cols)]
    finalTable = []
    for i in range(len(table[0])):
        for k in range(len(colWidths)):
            rowNew[i].append(table[k][i])
        finalTable.append(separator.join(rowNew[i]))

    finalTable2 = '\n'.join(finalTable)
    print(finalTable2)


printTable(tableData)