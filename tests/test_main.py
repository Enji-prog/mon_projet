import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import addition

def test_addition():
    assert addition(2, 3) == 5
