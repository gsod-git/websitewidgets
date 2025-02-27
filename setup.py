# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# get version from version variable in erpnext/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

with open('websitewidgets/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='websitewidgets',
	version=version,
	description='Open Source ERP',
	author='Frappe Technologies',
	author_email='info@tridots.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
