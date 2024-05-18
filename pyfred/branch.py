from .leaf import Leaf

class Branch:
	def __init__(self, branch_name, leaves, api_key):
		self.branch_name = branch_name
		self.api_key = api_key
		self.leaves = {
			leaf_name: Leaf(branch_name, leaf_name, **leaf_info, api_key=api_key) for leaf_name, leaf_info in leaves.items()
			}

	def __getattr__(self, leaf_name):
		if leaf_name in self.leaves:
			return self.leaves[leaf_name]
		else:
			raise AttributeError(f'Branch {self.branch_name} has no leaf {leaf_name}')

