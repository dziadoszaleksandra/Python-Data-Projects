# Zadanie 5

import math

kwadraty = [x**2 for x in range(1, 101) if math.sqrt(x) == int(math.sqrt(x))]
print(kwadraty)
