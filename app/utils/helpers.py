# app/utils/helpers.py

import random
import string
from datetime import datetime, timedelta
from typing import Any

# -----------------------------
# Generate random string
# -----------------------------
def generate_random_string(length: int = 8) -> str:
    """
    Generates a random alphanumeric string of given length.
    Useful for temporary passwords, tokens, or IDs.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# -----------------------------
# Convert string to datetime
# -----------------------------
def str_to_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Converts a string to a datetime object based on the given format.
    """
    return datetime.strptime(date_str, fmt)


# -----------------------------
# Add minutes to datetime
# -----------------------------
def add_minutes_to_datetime(dt: datetime, minutes: int) -> datetime:
    """
    Adds given minutes to a datetime object and returns new datetime.
    """
    return dt + timedelta(minutes=minutes)


# -----------------------------
# Safe dictionary get
# -----------------------------
def safe_get(d: dict, key: Any, default: Any = None) -> Any:
    """
    Safely retrieves a value from a dictionary.
    Returns default if key is not found.
    """
    return d.get(key, default)
