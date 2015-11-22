# -*- encoding: utf-8 -*-


import os
import sys
sys.path.append(os.path.join(sys.path[0], '../'))

import nose

from app.handler.calculator import add

def test_first():
    assert '5' == add(4, 1)

if __name__ == "__main__":
    nose.runmodule()
