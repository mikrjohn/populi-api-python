#!/usr/bin/env python3

'''
Script to fix linting issues in the populi-api-python codebase
'''

import os

def fix_wildcard_imports(file_path):
    """Replace 'from x import *' with explicit imports"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace nose.tools wildcard imports in test files
    if 'from nose.tools import *' in content:
        content = content.replace('from nose.tools import *', 'import unittest')
    
    # Fix unused variable in driver_tests.py
    if 'driver_tests.py' in file_path and 'result = driver.request(' in content:
        content = content.replace('result = driver.request(', '_ = driver.request(')
    
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Fixed {file_path}")

def main():
    # Fix test files
    test_files = [
        'tests/build_tests.py',
        'tests/driver_tests.py',
        'tests/populi_tests.py'
    ]
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for test_file in test_files:
        file_path = os.path.join(base_dir, test_file)
        if os.path.exists(file_path):
            fix_wildcard_imports(file_path)

if __name__ == '__main__':
    main()
