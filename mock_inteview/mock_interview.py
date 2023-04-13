def row_sums(array):
   
    row_sums = []
    for row in array:
        row_sum = 0
        for val in row:
            row_sum += val
        row_sums.append(row_sum)
    return row_sums