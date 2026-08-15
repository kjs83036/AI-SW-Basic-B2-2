import pytest
from src.utils.string_ops import capitalize_words, reverse_string, strip_all_whitespace

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""

def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"
    assert strip_all_whitespace("hello \t\n world\r\n") == "helloworld"
    assert strip_all_whitespace("") == ""
