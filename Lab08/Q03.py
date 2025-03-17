#Update the first set with items that don’t exist in the second set
A={10, 20, 30, 40, 50}
B= {30, 40, 50, 60, 70}

A.difference_update(B) 
print(A) 
