# python1course/zaj01/__init__.py

# importing variables from skrypt2 (safe, no inputs)
from .skrypt2 import ja, lista

# importing variables from skrypt5
from .skrypt5 import jezyk, rok

# exporting these variables to be visible outside
__all__ = ["ja", "jezyk", "lista", "rok"]
