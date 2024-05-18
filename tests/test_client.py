import unittest
from pyfred.client import FredAPIClient

class TestFredAPIClient(unittest.TestCase):
	def setUp(self):
		self.api_key = 'test_key'
		self.client = FredAPIClient(self.api_key)

	def test_invalid_branch(self):
		with self.assertRaises(AttributeError):
			self.client.invalid_branch

	def test_valid_branch(self):
		self.assertIsNotNone(self.client.category)

if __name__ == '__main__':
	unittest.main()
