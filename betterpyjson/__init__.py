"""
"""

import json
from types import SimpleNamespace


def load_dict(obj):
	return load_str(json.dumps(obj))


def load_str(text):
	return json.loads(text, object_hook=lambda d: BetterPyJSON(**d))


class BetterPyJSON(SimpleNamespace):
	"""
	"""

	def __getitem__(self, key):
		"""
		Overload index operator.

		Args:
			key(object): Any valid Python object key.
		
		Returns:
			The corresponding object contained within this namespace.
		"""
		return getattr(self, key)

	def __len__(self):
		return len(self.attributes())

	def __setattr__(self, name, value):
		if self.__dict__.get(name, False):
			self.__dict__[name] = value

	def __repr__(self):
		return str(self.__dict__)

	def __iter__(self):
		return self.keys()

	def keys(self):
		for i in self.attributes():
			yield i

	def values(self):
		for i in self.attributes():
			yield self[i]

	def attributes(self):
		return list(set(dir(self)) - set(dir(BetterPyJSON)))
