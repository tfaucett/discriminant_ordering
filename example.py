import numpy as np
from discriminant_ordering import ADO

n_data = 5000
n_calc = 500
x = np.random.rand(n_data)
y = np.random.rand(n_data)
targets = np.random.randint(2, size=n_data)

# ADO calculated without statistics
print(ADO(fx=x, gx=y, target=targets, n_data=n_calc))

# ADO calculated with statistics (i.e. mean and stdev of ADO)
print(ADO(fx=x, gx=y, target=targets, n_data=n_calc, stats=True))

# ADO example where you expect perfect similarity (i.e. compare x with x)
print(ADO(fx=x, gx=x, target=targets, n_data=n_calc))
print(ADO(fx=x, gx=x, target=targets, n_data=n_calc, stats=True))