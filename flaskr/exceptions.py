class AppException(Exception):
    error_code = 0
    error_message = "Message is empty, please check."


class JwtTokenException(AppException):
    error_code = 401
    error_message = "There's an error of JWT token"


class JwtTokenNotFound(JwtTokenException):
    error_code = 401
    error_message = "JWT token is required"


class JwtTokenInvalid(JwtTokenException):
    error_code = 422
    error_message = "JWT token is invalid"


class InvalidFormInput(AppException):
    error_code = 400

    def __init__(self, error_message: str):
        self.error_message = error_message
        super().__init__()
