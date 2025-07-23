"""
PEP 378: Format Specifier for Thousands Separator
"""
import sys
import unittest
from decimal import Decimal

print(format(1234567, ',d'))
print(format(1234567.89, ',.2f'))

"""
Other Language Changes
"""
print(bin(100))
print(0b000111)
n = 2 ** 123 - 1
print(n.bit_length())
print((n + 1).bit_length())
print(round(1123, -2))

"""
New, Improved, and Deprecated Modules¶
"""
# The decimal module now supports methods for creating a decimal object from a binary float. The conversion is exact but
# can sometimes be surprising:
print(Decimal.from_float(1.1))

"""
The unittest module now supports skipping individual tests or classes of tests.
"""


class TestGizmo(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_gizmo_on_windows(self):
        pass

    @unittest.expectedFailure
    def test_gimzo_without_required_library(self):
        pass
