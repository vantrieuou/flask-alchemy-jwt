import time


def get_unique_email():
    return f"email{get_unique_id()}"


def get_unique_id():
    unique = hash(time.time())
    return unique
