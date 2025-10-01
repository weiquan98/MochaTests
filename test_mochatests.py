# test_mochatests.py
"""
Tests for MochaTests module.
"""

import unittest
from mochatests import MochaTests

class TestMochaTests(unittest.TestCase):
    """Test cases for MochaTests class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MochaTests()
        self.assertIsInstance(instance, MochaTests)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MochaTests()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
