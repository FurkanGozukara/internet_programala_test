# Demonstrating robust floating-point comparisons using numpy.isclose()

import numpy as np


gg = "test"
value = 32

tag1 = "test"

value4 = 4
valu3 = 3
value1 = 0.1 + 0.2 # Will not be exactly 0.3 due to rounding errors
value2 = 0.3

print(f"Value 1 (0.1 + 0.2): {value1}")
print(f"Value 2 (0.3): {value2}")

value6=6

# Problematic direct equality comparison (will be False)
if value1 == value2:
    print("Direct comparison (==): Value 1 == Value 2 (True - Incorrect)")
else:
    print("Direct comparison (==): Value 1 == Value 2 (False - Correctly False)") # We expect this

# Robust comparison using numpy.isclose() with default tolerances
if np.isclose(value1, value2):
    print("numpy.isclose() with defaults: Value 1 is close to Value 2 (True - Correct)") # We expect this
else:
    print("numpy.isclose() with defaults: Value 1 is close to Value 2 (False - Incorrect)")

# Customizing tolerances - more strict relative tolerance
rtol_strict = 1e-28 # Tighter relative tolerance
if np.isclose(value1, value2,rtol=rtol_strict, atol=rtol_strict):
    print(f"numpy.isclose() with rtol={rtol_strict}: Value 1 is close to Value 2 (True)")
else:
    print(f"numpy.isclose() with rtol={rtol_strict}: Value 1 is close to Value 2 (False)") # Might become False with stricter tolerance

# Customizing tolerances - adding absolute tolerance
atol_non_zero = 1e-07 # Non-zero absolute tolerance
if np.isclose(value1, value2, atol=atol_non_zero):
    print(f"numpy.isclose() with atol={atol_non_zero}: Value 1 is close to Value 2 (True)") # Likely True
else:
    print(f"numpy.isclose() with atol={atol_non_zero}: Value 1 is close to Value 2 (False)")

# Example with arrays - element-wise comparison
array1 = np.array([0.9999, 2.0000001, 3.0])
array2 = np.array([1.0, 2.0, 3.0000002])

close_array = np.isclose(array1, array2) # Element-wise comparison of arrays
print(f"\nArray 1: {array1}")
print(f"Array 2: {array2}")
print(f"numpy.isclose() element-wise array comparison: {close_array}") # Boolean array indicating element-wise closeness
