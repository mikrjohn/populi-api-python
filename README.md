# Populi

This module interacts with the Populi API, handling pagination, and rate limiting using pycurl.
Most every command found in the [Populi API Reference](https://support.populiweb.com/hc/en-us/articles/223798747#getAcademicTerms) can be accessed via pythonic methods. I have attempted to keep the two in sync.

## Example
```python
import populi

populi.initialize(
    endpoint='https://example_campus.populi.web.com/api/index.php',
    access_key='example access key',
    asXML=True  # Now determines if responses are returned as native Python objects
)

# returns transactions as a Python dictionary
results = populi.get_transactions(start_date='2012-10-01', end_date='2012-10-02')

# Or get results as a JSON string
populi.initialize(
    endpoint='https://example_campus.populi.web.com/api/index.php',
    access_key='example access key',
    asXML=False
)
json_results = populi.get_transactions(start_date='2012-10-01', end_date='2012-10-02')
```

## Features

- Full support for the JSON-based Populi API
- Automatic pagination for large result sets
- Flexible response formats (JSON string or native Python objects)
- Robust error handling
- Rate limiting with automatic retry

## Versions

### 0.1.0
+ Updated library to use the new JSON-based Populi API
+ Changed `asXML` parameter to control returning native Python objects vs JSON strings
+ Added new error types for the JSON API
+ Improved pagination handling for JSON responses

### 0.0.7
+ Enabled passing curl options via initialize(). The added option list is in the format of tuples: (pycurl.OPTION, value).

### 0.0.6
+ Updated Command list as of commands shown on populi on May 25th, 2020
+ Fixed downloadFile and downloadBackup to return bytes.
