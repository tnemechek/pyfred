import unittest
from pyfred.branch import Branch

class TestBranch(unittest.TestCase):
	def setUp(self):
		self.api_key = 'test_key'
		self.branch_name = 'category'
		self.leaves = {
			'children': {
				'required_params': ['category_id'],
				'optional_params': ['realtime_start', 'realtime_end']
				}
			}
		self.branch = Branch(
			self.branch_name,
			self.leaves,
			self.api_key
			)

	def test_invalid_leaf(self):
		with self.assertRaises(AttributeError):
			self.branch.invalid_leaf

	def test_valid_leaf(self):
		self.assertIsNotNone(self.branch.children)

if __name__ == '__main__':
	unittest.main()
