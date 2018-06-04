a = "India is a great country with a lot of heritage"
b = "South Africa is a great country with a lot of freedom"

def test(a, b):                    # Defining a Procedure
    x = a.split()                  # ['India', 'is', 'a', 'great', 'country', 'with', 'a', 'lot', 'of', 'heritage']
    y = b.split()                  # ['South', 'Africa', 'is', 'a', 'great', 'country', 'with', 'a', 'lot', 'of', 'freedom']
    list = []                      # Creating a Variable with Empty List
    for i in x:                    # "i" will get individual values in X
        if i not in y:             # If "i" (individual values of X) is not in Y
            list.append(i)         # Then append values to empty list we created
    for j in y:
        if j not in x:
            list.append(j)
    return (" ".join(list))        # Returning empty list as a string
    
print (test(a, b))

# CODED BY - GAURAV PADAWE
