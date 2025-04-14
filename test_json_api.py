#!/usr/bin/env python3
"""
Test script for the updated Populi API client with JSON support.
"""

import populi
import json
import sys
import os

def main():
    # Get API credentials from environment or command line
    endpoint = os.environ.get('POPULI_ENDPOINT', '')
    access_key = os.environ.get('POPULI_KEY', '')
    
    if len(sys.argv) > 1:
        endpoint = sys.argv[1]
    if len(sys.argv) > 2:
        access_key = sys.argv[2]
    
    if not endpoint or not access_key:
        print("Usage: python test_json_api.py [endpoint] [access_key]")
        print("Or set POPULI_ENDPOINT and POPULI_KEY environment variables")
        return
    
    print(f"Testing Populi JSON API client with endpoint: {endpoint}")
    
    # Test with native Python objects
    print("\n=== Testing with native Python objects ===")
    populi.initialize(
        endpoint=endpoint,
        access_key=access_key,
        asXML=True  # Now means "return native Python objects"
    )
    
    try:
        # Test a basic API call
        print("Getting academic terms...")
        terms = populi.get_academic_terms()
        print(f"Received {len(terms)} academic terms")
        if terms:
            print(f"First term: {terms[0]['name'] if isinstance(terms, list) else terms}")
        
        # Test a paginated API call if available
        print("\nGetting students...")
        students = populi.get_term_students()
        print(f"Received student data of type: {type(students)}")
        if isinstance(students, dict) and 'students' in students:
            print(f"Found {len(students['students'])} students")
        elif isinstance(students, list):
            print(f"Found {len(students)} students")
        else:
            print(f"Unexpected response format: {type(students)}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    # Test with JSON string response
    print("\n=== Testing with JSON string response ===")
    populi.initialize(
        endpoint=endpoint,
        access_key=access_key,
        asXML=False  # Return JSON strings
    )
    
    try:
        # Test a basic API call
        print("Getting academic terms as JSON...")
        terms_json = populi.get_academic_terms()
        terms = json.loads(terms_json)
        print(f"Received JSON string of length: {len(terms_json)}")
        if terms:
            print(f"First term: {terms[0]['name'] if isinstance(terms, list) else terms}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
