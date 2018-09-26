import logging
import unittest
from cyclic import Cyclic


LOGGER_NAME = 'cyclic-'
log = logging.getLogger(LOGGER_NAME)


class TestMethods(unittest.TestCase):
    
    def test_default(self):
        cy = Cyclic()
        # just taking some names
        A = 1
        B = 2
        C = 3
        D = 4
        
        # Let's say A is a prent of B
        cy.add(B, A)
        
        # B is a parent of C
        cy.add(C, B)
        
        # C is a parent of A (cyclic)
        cy.add(A, C)
        
        # let's see if C is in any kind of cyclic relation
        
        self.assertTrue(cy.is_cyclic(C))
        
        # let's see if A is in any kind of cyclic relation
        self.assertTrue(cy.is_cyclic(A))
        
        # Now let's say D is a parent of B
        cy.add(B, D)
        
        self.assertFalse(cy.is_cyclic(D))
        
        # Now, say D is a parent of A
        cy.add(A, D)
        
        # D is a super parent now,
        self.assertFalse(cy.is_cyclic(D))
        
        # let's say D is the child of C
        cy.add(D, C)
        
        self.assertTrue(cy.is_cyclic(D))
        
        

if __name__ == "__main__":
    unittest.main()
