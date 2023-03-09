from setuptools import setup, find_packages

console_scripts = [
]

long_description = """

"""

setup(
    name='mk-blender-scr',
    packages=find_packages(),
    install_requires=['ase', 'nglview', 'jinja2'], 
    version='1.0',
    author='Kato Taisetsu',
    url='',
    description='Create a Python script for Blender from Atoms of ASE.',
    long_description=long_description,
    long_description_content_type='text/markdown', # 'text/plain', 'text/x-rst', 'text/markdown'
    keywords='blender ase',
    entry_points={'console_scripts': console_scripts},
)