table = [['Amount1','Amount2', 'Amount3'],
         [  321,       43,       432],
         [ 3213,       42,       482],
         [  543,        38,      232]]

def row_totals(table, *, header=True):
    if header: 
        table = table[1:]
        
    return map(sum, table)

def row_totals(table, *, header=True):
    if header: 
        table = table[1:]
        
    return [sum(row)for row in table]

print(row_totals(table))