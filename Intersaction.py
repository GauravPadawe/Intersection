a = "India is a great country with a lot of heritage"
b = "South Africa is a great country with a lot of freedom"

x = a.split()                # ['India', 'is', 'a', 'great', 'country', 'with', 'a', 'lot', 'of', 'heritage']
y = b.split()                # ['South', 'Africa', 'is', 'a', 'great', 'country', 'with', 'a', 'lot', 'of', 'freedom']

a = x                        # Assigning X's value to A
b = y                        # Assigning Y's value to B

def test(a, b):                     # Defining a Procedure
	list = [ ]                      # Creating a Variable with Empty List
	for i in b:                     # i will get individual values in B
		if i not in a:              # If i (individual values of B) is not in A , i.e, ['South', 'Africa', 'freedom']
			list.append(i)          # Then append ['South', 'Africa', 'freedom'] to empty list we created
	for j in a:                     # Similary, j will get individual values in A
		if j not in b:              # If j (individual values of A) is not in B , i.e, ['India', 'heritage']
			list.append(j)          # Then append ['India', 'heritage'] to empty list
	return (' '.join(list))         # returning empty list as a string
	
print (test(a, b))

# CODED BY - GAURAV PADAWE
