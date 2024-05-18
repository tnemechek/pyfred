import os
from dotenv import load_dotenv
from .branch import Branch
from .fred_helper import fred_hierarchy

load_dotenv()

class FredAPIClient:
	def __init__(self, api_key=None):
		self.api_key = api_key or os.getenv('FRED_API_KEY')
		if not self.api_key:
			raise ValueError('No API key provided. Key must be passed as a parameter or stored in the ".env" file.')
		self.branches = {
			branch_name: Branch(branch_name, leaves, api_key) for branch_name, leaves in fred_hierarchy.items()
			}

	def __getattr__(self, branch_name):
		if branch_name in self.branches:
			return self.branches[branch_name]
		raise AttributeError(f'Branch {branch_name} not found in FredAPI branches.')
