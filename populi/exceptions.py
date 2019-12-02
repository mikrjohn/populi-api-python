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


exception_lookup = dict(
    AUTHENTICATION_ERROR=AuthenticationError,
    UNKNOWN_TASK=UnknownTask,
    BAD_PARAMETER=BadParameter,
    LOCKED_OUT=LockedOut,
    PERMISSION_ERROR=PermissionError,
    OTHER_ERROR=OtherError
)