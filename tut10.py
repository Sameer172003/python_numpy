# The Difference Between Copy and View in numpy array

import numpy as np

var=np.array([1,2,3,4,5])
dup=np.copy(var)    # Copy function
view=var.view()     # View function
print(dup)
print()
print(view)

