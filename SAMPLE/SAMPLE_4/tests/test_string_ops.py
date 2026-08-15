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
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("") == ""

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""

def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"
    assert strip_all_whitespace("a\t\nb\r\n c") == "abc"
    assert strip_all_whitespace("") == ""

def test_to_snake_case():
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("HelloWorldTest") == "hello_world_test"
    assert to_snake_case("hello-world test") == "hello_world_test"

def test_slugify():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("Python & Git: Best Practice") == "python-git-best-practice"
    assert slugify("") == ""

def test_truncate_words():
    text = "The quick brown fox jumps over the lazy dog"
    assert truncate_words(text, 4) == "The quick brown fox..."
    assert truncate_words(text, 10) == text
    assert truncate_words(text, 2, suffix=" [more]") == "The quick [more]"
