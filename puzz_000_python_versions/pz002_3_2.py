import argparse
import collections
import concurrent
import math
import shutil
from datetime import datetime, timezone
from itertools import accumulate

"""Python 3.2, 20 February 2011"""

print("Python 3.2")

"""PEP 389: Argparse Command Line Parsing Module"""
parser = argparse.ArgumentParser(
    description='Manage servers',
    epilog='Tested on Solaris and Linux')

"""PEP 3148: The concurrent.futures module¶"""
# with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
#     e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
#     e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
#     e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
#     e.submit(shutil.copy, 'src3.txt', 'dest4.txt')


"""PEP 3147: PYC Repository Directories

Python’s scheme for caching bytecode in .pyc files did not work well in environments with multiple Python interpreters. 
If one interpreter encountered a cached file created by another interpreter, it would recompile the source and overwrite 
the cached file, thus losing the benefits of caching.

The issue of “pyc fights” has become more pronounced as it has become commonplace for Linux distributions to ship with 
multiple versions of Python. These conflicts also arise with CPython alternatives such as Unladen Swallow.

To solve this problem, Python’s import machinery has been extended to use distinct filenames for each interpreter. 
Instead of Python 3.2 and Python 3.3 and Unladen Swallow each competing for a file called “mymodule.pyc”, they will now 
look for “mymodule.cpython-32.pyc”, “mymodule.cpython-33.pyc”, and “mymodule.unladen10.pyc”. And to prevent all of these 
new files from cluttering source directories, the pyc files are now collected in a “__pycache__” directory stored under 
the package directory.
"""
print(collections.__cached__)

"""The hasattr() function works by calling getattr()"""


class A:
    @property
    def f(self):
        return 1 // 0


a = A()
# hasattr(a, 'f') #ZeroDivisionError: integer division or modulo by zero

"""The str() of a float or complex number is now the same as its repr()."""
print(repr(math.pi))
print(str(math.pi))

"""range objects now support index and count methods. 
The count method for the range object returns the number of times the number
specified in the argument occurs in the sequence.
"""
print(range(0, 100, 2).count(98))

"""accumulate"""
prob_dist = [0.1, 0.4, 0.2, 0.3]
print(list(accumulate(prob_dist)))  # [0.1, 0.5, 0.7, 1.0]

"""deque"""
d = collections.deque('simsalabim')
print(d)
print(d.count('s'))
d.reverse()
print(d)

"""datetime and time"""
print(datetime.now(timezone.utc))
print(datetime.now())
