from setuptools import setup, find_packages

setup(
	name='pyfred',
	version='0.1',
	packages=find_packages(),
	install_requires=[
		'requests',
		'pandas'
		'python-dotenv'
		],
	author='Thomas Nemechek',
	description='Python wrapper for the US Federal Reserve FRED API',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/tnemechek/pyfred',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		],
	python_requires='>=3.6'
	)
