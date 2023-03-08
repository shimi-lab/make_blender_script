from setuptools import setup, find_packages

console_scripts = [
]

setup(
    name='grrmpy',
    version='1.0',
    packages=find_packages(),
    entry_points={'console_scripts': console_scripts},
)