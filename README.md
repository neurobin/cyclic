[![Build Status](https://travis-ci.org/neurobin/cyclic.svg?branch=release)](https://travis-ci.org/neurobin/cyclic)

Handle cyclic relation compared by value.

# Install

Install from Pypi:

```bash
pip install cyclic
```

# Usage

```python
from cyclic import Cyclic

cy = Cyclic()

# Let's say A is a prent of B
cy.add(B, A)

# B is a parent of C
cy.add(C, B)

# C is a parent of A (cyclic)
cy.add(A, C)

# let's see if C is in any kind of cyclic relation

print(cy.is_cyclic(C)) # True

```
