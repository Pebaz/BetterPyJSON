"""
"""

from types import SimpleNamespace


class BetterPyJSON(SimpleNamespace):
	def __getitem__(self, key):
		"""
		Overload index operator.

		Args:
			key(object): Any valid Python object key.
		
		Returns:
			The corresponding object contained within this namespace.
		"""
		return getattr(self, key)

	def keys(self):
		for i in self.attributes():
			yield i

	def values(self):
		for i in self.attributes():
			yield self[i]

	def __iter__(self):
		return self.keys()

	def attributes(self):
		return list(set(dir(self)) - set(dir(SwaggerModel)))

	def __len__(self):
		return len(self.attributes())
