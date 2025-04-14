class BasePopuliException(Exception):
    pass


class AuthenticationError(BasePopuliException):
    pass


class UnknownTask(BasePopuliException):
    pass


class BadParameter(BasePopuliException):
    pass


class LockedOut(BasePopuliException):
    pass


class PermissionError(BasePopuliException):
    pass


class OtherError(BasePopuliException):
    pass


class TooManyRequests(BasePopuliException):
    pass


class APIVersionError(BasePopuliException):
    pass


class RateLimitError(BasePopuliException):
    pass


class InvalidJSONError(BasePopuliException):
    pass


# Map Populi API error codes to exception classes
exception_lookup = dict(
    AUTHENTICATION_ERROR=AuthenticationError,
    UNKNOWN_TASK=UnknownTask,
    BAD_PARAMETER=BadParameter,
    LOCKED_OUT=LockedOut,
    PERMISSION_ERROR=PermissionError,
    RATE_LIMIT_ERROR=RateLimitError,
    API_VERSION_ERROR=APIVersionError,
    INVALID_JSON=InvalidJSONError,
    OTHER_ERROR=OtherError
)
