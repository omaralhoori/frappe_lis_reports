from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lis_reports/__init__.py
from lis_reports import __version__ as version

setup(
	name="lis_reports",
	version=version,
	description="Lis",
	author="omar",
	author_email="omar",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
