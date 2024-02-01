

def find_max(input_ar):
    if len(input_ar) < 2:
        return input_ar[0]
    
    #recursive case
    a = input_ar[0]
    b = input_ar[1]

    bigger = a if a > b else b
    sliced_ar = input_ar[2:]
    sliced_ar.append(bigger)
    return find_max(sliced_ar)


input_ar = [ 3, 5, 1, 7]
print(find_max(input_ar))