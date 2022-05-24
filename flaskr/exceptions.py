class JwtTokenException(Exception):
    error_code = 401
    error_message = "There's an error of JWT token"


class JwtTokenNotFound(JwtTokenException):
    error_message = "JWT token is required"


class JwtTokenInvalid(JwtTokenException):
    error_code = 422
    error_message = "JWT token is invalid"
