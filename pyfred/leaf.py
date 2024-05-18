import requests
import pandas as pd
from fred_helper import baseurl_fred


class Leaf:
	def __init__(self, branch, leaf_name, required_params, optional_params, api_key):
		self.branch = branch
		self.leaf_name = leaf_name
		self.required_params = required_params
		self.optional_params = optional_params
		self.api_key = api_key
		self.url = '/'.join([baseurl_fred, branch, leaf_name])
		self.params = {'api_key': self.api_key, 'file_type': 'json'}

	def make_params(self, **kwargs):
		for param in self.required_params:
			if param not in kwargs:
				raise ValueError(f'Missing required parameter: {param}')
		for param, value in kwargs.items():
			if param in self.required_params + self.optional_params:
				self.params[param] = value
		return self.params

	def get_data(self, **kwargs):
		self.make_params(**kwargs)
		response = requests.get(self.url, params=self.params)
		response.raise_for_status()
		return response.json()

	def get_dataframe(self, **kwargs):
		data = self.get_data(**kwargs)
		self.frame = pd.DataFrame(data)
		return self.frame


