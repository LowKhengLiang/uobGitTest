import pytest
from hello_world import hello_word

def test_hello_world():
  assert hello_world() == "Hello, World!"
  
