import os

def test_file_exists():
    assert os.path.exists("data/input.txt")