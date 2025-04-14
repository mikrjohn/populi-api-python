# Populi Python API Client

A comprehensive Python library for interacting with the [Populi](https://www.populiweb.com/) API. This module makes it easy to access and manipulate data from your Populi instance through a clean, Pythonic interface that handles authentication, pagination, rate limiting, and response formatting.

## Overview

This library provides a Python wrapper for the complete Populi API, allowing developers to programmatically access student information, course data, financial records, and other information stored in Populi. It's designed to simplify integration with Populi's web services by handling the low-level details of API interaction.

## Features

- **Complete API Coverage**: Implements all commands from the [Populi API Reference](https://support.populiweb.com/hc/en-us/articles/223798747-API-Reference)
- **Automatic Pagination**: Seamlessly handles multi-page results
- **Response Format Options**: Return data as either JSON strings or Python objects
- **Error Handling**: Custom exceptions for different API error types
- **Rate Limiting**: Automatic retry with exponential backoff for rate-limited requests
- **Flexible Authentication**: Support for both access key and username/password authentication

## Installation

```bash
pip install populi-mrobison
```

### Requirements

- Python 3.x
- pycurl
- beautifulsoup4 (for building from the API reference)

## Setup

Initialize the library with your Populi credentials:

```python
import populi

# Using access key with native Python objects returned
populi.initialize(
    endpoint='https://your_campus.populiweb.com/api/index.php',
    access_key='your_access_key',
    asXML=True  # Set to True to get Python objects instead of JSON strings
)

# OR using username and password with JSON string responses
populi.initialize(
    endpoint='https://your_campus.populiweb.com/api/index.php',
    username='your_username',
    password='your_password',
    asXML=False  # Return JSON strings
)

# You can also pass additional curl options
populi.initialize(
    endpoint='https://your_campus.populiweb.com/api/index.php',
    access_key='your_access_key',
    curl_options=[
        (pycurl.CONNECTTIMEOUT, 30),
        (pycurl.TIMEOUT, 60)
    ]
)
```

## Usage Examples

### Get Person Information

```python
# Get person details by ID (returned as a Python dictionary)
person = populi.get_person(person_id='12345')

# Get person details by student ID
student = populi.get_person(student_id='S12345')

# Include profile image data
person_with_image = populi.get_person(person_id='12345', return_image_data='1')
```

### Financial Transactions

```python
# Get transactions in a date range
transactions = populi.get_transactions(
    start_date='2023-01-01',
    end_date='2023-06-30'
)

# Get transactions for a specific person
person_transactions = populi.get_transactions(primary_actor_id='12345')

# Get account ledger entries
ledger_entries = populi.get_entries_for_account(
    account_id='1000',
    start_date='2023-01-01',
    end_date='2023-06-30'
)
```

### Course Information

```python
# Get a course instance
course = populi.get_course_instance(instance_id='12345')

# Get assignments for a course
assignments = populi.get_course_instance_assignments(instance_id='12345')

# Get students enrolled in a course
students = populi.get_course_instance_students(instance_id='12345')
```

### Adding and Updating Data

```python
# Add a new person
new_person = populi.add_person(
    first_name='John',
    last_name='Doe',
    gender='MALE',
    birth_date='1990-01-01'
)

# Add a tag to a person
populi.add_tag(
    person_id='12345',
    tag='Important Donor'
)

# Update a phone number
populi.update_phone_number(
    phoneid='12345',
    phone_number='555-123-4567',
    type='MOBILE',
    primary='1'
)
```

### Working with Donations

```python
# Add a donation
donation = populi.add_donation(
    amount='100.00',
    fund_id='123',
    payment_method='CREDIT_CARD',
    person_id='12345'
)

# Get donor information
donor = populi.get_donor(person_id='12345')
```

### File Operations

```python
# Download a file
file_content = populi.download_file(file_id='12345')

# Upload a file to a person's profile
populi.upload_file(
    person_id='12345',
    file=my_file_data
)
```

## JSON Response Handling

The updated library now handles JSON responses from the Populi API. You can choose how to receive the responses:

```python
# Get responses as native Python objects (dictionaries or lists)
populi.initialize(endpoint='your_endpoint', access_key='your_key', asXML=True)

# Work with Python objects directly
students = populi.get_term_students()
for student in students.get('students', []):
    print(f"Student: {student['first_name']} {student['last_name']}")

# Or get responses as JSON strings
populi.initialize(endpoint='your_endpoint', access_key='your_key', asXML=False)

# Parse the JSON yourself if needed
import json
students_json = populi.get_term_students()
students_data = json.loads(students_json)
```

## Error Handling

The library provides custom exceptions for different API error types:

```python
import populi
from populi.exceptions import AuthenticationError, LockedOut, PermissionError, RateLimitError

try:
    result = populi.get_person(person_id='12345')
except AuthenticationError:
    print("Authentication failed")
except LockedOut:
    print("Your account is locked")
except PermissionError:
    print("You don't have permission to access this resource")
except RateLimitError:
    print("API rate limit exceeded")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Advanced Usage

### Building from API Reference

The library includes tooling to automatically generate command wrappers from the Populi API Reference:

```python
from populi import build
import autopep8

# Generate commands from the API reference
commands = build.get_commands()

# Generate code for a new cmds.py
output = build.imports
for command in commands:
    output += "\n"
    output += str(command)
    output += "\n\n"

formatted_output = autopep8.fix_code(output, options={'aggressive': 2})
print(formatted_output)
```

## Pagination

The library handles pagination automatically for endpoints that return large result sets:

```python
# This will automatically fetch all pages and combine them into a single result
all_transactions = populi.get_transactions(start_date='2023-01-01', end_date='2023-12-31')

# For endpoints with pagination, use the root_element parameter to identify the array of results
all_people = populi.get_term_students(term_id='12345')
```

## Limitations

- The library is subject to Populi's API rate limits
- Complex data structures like arrays may require special handling
- Some operations may require specific permissions in your Populi instance

## Migration from XML to JSON

If you're upgrading from a previous version that used XML responses, note these changes:

1. The `asXML` parameter now controls whether you get native Python objects (True) or JSON strings (False)
2. Response handling code should be updated to use Python dictionaries instead of XML elements
3. XPath queries should be replaced with dictionary access

Example of migrating code:

```python
# Old XML-based code
students = populi.get_term_students(term_id='12345')
for student in students.findall('student'):
    print(student.find('first_name').text, student.find('last_name').text)

# New JSON-based code
students = populi.get_term_students(term_id='12345')
for student in students.get('students', []):
    print(student.get('first_name'), student.get('last_name'))
```

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
