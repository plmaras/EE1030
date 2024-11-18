import numpy as np
a = np.random.randint(100,size =(40,40))
for row in a:
    print(row)
b = np.linalg.eigvals(a)

print("\n",b,"\n")
