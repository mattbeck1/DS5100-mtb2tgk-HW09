from setuptools import setup

setup(
    name = 'books',
    version = '0.1.0',
    author = 'Matthew Beck',
    author_email = 'mtb2tgk@virginia.edu',
    packages = ['books'],
    url = 'https://github.com/mattbeck1/DS5100-mtb2tgk-HW09/blob/main/hw09.ipynb',
    license = 'LICENSE.txt',
    description = 'An awesome package with the booklover module',
    install_requires = [
        "pandas >= 2.2.2",
        "numpy >= 1.26.4",
    ],
)