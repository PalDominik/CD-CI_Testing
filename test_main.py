import unittest
from main import Szamolas

class TestAdd(unittest.TestCase):
    def test_hozaadd_majd_kivon(self):
        self.assertEqual(Szamolas(2,3,1),4)

    def test_minusz_eredmeny(self):
        self.assertEqual(Szamolas(1,1,3), -1)

if __name__ == "__main__":
    unittest.main()