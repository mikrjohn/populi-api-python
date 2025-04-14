from .cmds import (
    # Core functions
    initialize,
    get_anonymous,
    get_all_anonymous,
    # Common API functions - add more as needed
    get_academic_terms,
    get_term_students,
    add_address,
    add_email_address,
    add_enrollment,
    # Add any other functions you regularly use
)

# Define public API
__all__ = [
    "initialize",
    "get_anonymous",
    "get_all_anonymous",
    "get_academic_terms",
    "get_term_students",
    "add_address",
    "add_email_address",
    "add_enrollment",
]

name = "populi"
