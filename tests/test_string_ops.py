import pytest
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    strip_all_whitespace,
    to_snake_case,
    slugify,
    truncate_words,
)


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""


def test_reverse_string():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""


def test_strip_all_whitespace():
    assert strip_all_whitespace("  hello   world \n \t") == "helloworld"
    assert strip_all_whitespace("") == ""


def test_to_snake_case():
    assert to_snake_case("camelCaseString") == "camel_case_string"
    assert to_snake_case("PascalCase") == "pascal_case"
    assert to_snake_case("hello-world test") == "hello_world_test"


def test_slugify():
    assert slugify("Hello World! @2026") == "hello-world-2026"
    assert slugify("  Git & GitHub Best Practices  ") == "git-github-best-practices"


def test_truncate_words():
    text = "The quick brown fox jumps over the lazy dog"
    assert truncate_words(text, 4) == "The quick brown fox..."
    assert truncate_words("Short text", 5) == "Short text"
