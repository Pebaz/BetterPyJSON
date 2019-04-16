import sys; sys.path.append('.')  # Ensure tests can see betterpyjson package
from betterpyjson import *


def test_creation():
	obj = load_dict(dict(name='Pebaz', age=24))
	assert obj.name == 'Pebaz'
	assert obj.age  == 24


def test___repr__():
	obj = load_dict(dict(name='Pebaz', age=24))
	assert str(obj) == "{'name': 'Pebaz', 'age': 24}"


def test_assignment():
	obj = load_dict(dict(name='Pebaz', age=24))
	obj.age = 32
	assert obj.age == 32


def test___iter__():
	obj = load_dict(dict(name='Pebaz', age=24))
	assert set(obj.keys())   == {'name', 'age'}
	assert set(obj.values()) == {'Pebaz', 24}

