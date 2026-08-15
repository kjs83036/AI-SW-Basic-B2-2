"""Utility package integrating Math, String, and Date helpers."""

from src.utils.date_ops import (
    add_days_to_date,
    calculate_days_between,
    format_iso_date,
    get_relative_time_string,
    parse_date_string,
)
from src.utils.math_ops import (
    add,
    calculate_average,
    divide,
    multiply,
    power,
    subtract,
)
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    slugify,
    strip_all_whitespace,
    to_snake_case,
    truncate_words,
)

__all__ = [
    # Math ops
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "calculate_average",
    # String ops
    "capitalize_words",
    "reverse_string",
    "strip_all_whitespace",
    "to_snake_case",
    "slugify",
    "truncate_words",
    # Date ops
    "format_iso_date",
    "parse_date_string",
    "add_days_to_date",
    "calculate_days_between",
    "get_relative_time_string",
]
