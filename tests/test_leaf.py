import unittest
from pyfred.leaf import Leaf

class TestLeaf(unittest.TestCase):
	def setUp(self):
		self.api_key = 'test_key'
		self.leaf = Leaf(
			'category',
			'children',
			['category_id'],
			['realtime_start', 'realtime_end'],
			self.api_key
			)

	def test_missing_required_param(self):
		with self.assertRaises(ValueError):
			self.leaf.get_data()

	def test_valid_request(self):
		self.leaf.get_data(category_id=0)
		self.assertIsNotNone(self.leaf.params)

if __name__ == '__main__':
	unittest.main()
