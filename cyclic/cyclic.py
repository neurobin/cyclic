"""
==================================================================
                    module cyclic
==================================================================

See <https://github.com/neurobin/cyclic> for documentation.

Copyright Md. Jahidul Hamid <jahidulhamid@yahoo.com>

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
"""

from .version import __version__

class Cyclic(object):
    """A class to handle cyclic relations. Compares by value.
    
    Procedure:
        
        Just add child parent relations with the add() method
        and test if any child has any cyclic relations calling is_cyclic()
    
    """

    def __init__(self):
        self.root = {}

    def is_cyclic(self, child):
        """Return True if child has any cyclic relation otherwise return False"""
        if child in self.root:
            if child in self.root[child]:
                return True
            else:
                for parent in self.root[child]:
                    if parent in self.root and child in self.root[parent]:
                        return True
        return False

    def add(self, child, parent):
        """Add a relation like child > parent """
        parentl = set([parent]) if parent else set()

        if child in self.root:
            self.root[child].update(parentl)
        else:
            self.root[child] = parentl
        
        if parent in self.root:
            # parent's parents are also the child's parents
            self.root[child].update(self.root[parent])
