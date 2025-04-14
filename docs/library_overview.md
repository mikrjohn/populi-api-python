# Populi Python API Library Overview

This is a Python library for interacting with the Populi API, providing a comprehensive wrapper around Populi's web-based API endpoints. Populi is a student information system/college management software, and this library allows programmatic access to its data and functionality.

## Main Purpose

The library serves as a client for the Populi API, handling authentication, request formatting, error management, and response parsing. It enables developers to interact with Populi's data programmatically rather than through the web interface.

## Key Features

1. **Complete API Coverage**: Implements wrapper functions for all Populi API endpoints documented in their official reference.

2. **Authentication Handling**: Supports access via both username/password and access key methods.

3. **Pagination Management**: Automatically handles paginated results for endpoints that return large datasets.

4. **Rate Limiting**: Implements retry logic for handling rate limits from the Populi API.

5. **Flexible Response Formats**: Returns data as either JSON strings or as native Python objects (dictionaries and lists).

6. **Comprehensive Error Handling**: Custom exceptions for different API error types.

7. **Auto-generated Command Interface**: The library command structure is automatically generated from the Populi API documentation.

## Architecture

The library is organized into several modules:

1. **driver.py**: The core module that manages HTTP requests to the Populi API using pycurl. It handles authentication, request formatting, and response parsing.

2. **cmds.py**: Contains all API command functions that users will primarily interact with. These functions are essentially wrappers around the core request functionality.

3. **build.py**: A utility for automatically generating the command functions by scraping and parsing the Populi API documentation website.

4. **exceptions.py**: Defines custom exception classes for different API error types.

The typical usage flow involves:

1. Initializing the library with credentials using `populi.initialize()`
2. Calling specific API methods like `populi.get_person()` or `populi.get_transactions()`
3. Processing the returned data (either as JSON strings or Python objects)

The library also includes a comprehensive test suite to ensure functionality and compatibility.

## Recent Updates

The library has been updated to work with Populi's JSON-based API instead of the previous XML-based API. Key changes include:

1. Response data is now returned as JSON strings or native Python objects (dictionaries and lists)
2. The `asXML` parameter now determines whether responses are returned as native Python objects (True) or JSON strings (False)
3. Improved error handling for JSON API responses
4. Enhanced pagination handling for JSON data structures

## Notable Design Patterns

1. **Command Pattern**: Each API endpoint is represented as a function that constructs the appropriate request parameters.

2. **Factory Pattern**: The build module dynamically generates command functions based on the API documentation.

3. **Singleton Pattern**: The driver module maintains a single instance for managing API connectivity.

4. **Adapter Pattern**: The library adapts between different response formats (JSON/Python objects) based on user preference.

This library would be particularly useful for educational institutions using Populi who need to integrate with other systems, automate workflows, or build custom reporting tools.
