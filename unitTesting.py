import unittest
from cmath import log10, pi
import struct
def area(struct):
    if(len(struct) > 1):
        area = 1
    else:
        area = pi
    for i in range(0,len(struct)):
        area = area * struct[i]
    area = round(area,2)
    return area

class TestCuboid(unittest.TestCase):
    
    def test(self):
        figura = 1
        l1 = 3.3
        lados = struct.unpack('f', struct.pack('f', l1))
        self.assertAlmostEqual(area(lados), 10.37)
    def test2(self):
        figura = 1
        l1 = 3.3
        l2 = 1
        lados = struct.unpack('ff', struct.pack('ff', l1,l2))
        self.assertAlmostEqual(area(lados), 3.3)
    def test23(self):
        figura = 1
        l1 = 3.3
        l2 = 1
        l3 = 19
        lados = struct.unpack('fff', struct.pack('fff', l1,l2,l3))
        self.assertAlmostEqual(area(lados), 62.7)
    
if __name__ == '__main__':
    unittest.main()