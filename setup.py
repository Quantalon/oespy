from setuptools import setup, find_packages


setup(
    name='oespy',
    version='0.2',
    description='OES Python Lib',
    long_description='OES Python Lib',
    long_description_content_type="text/markdown",
    python_requires=">=3.10.0",
    packages=find_packages(),
    include_package_data=True
)
