from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

with open('README.rst',encoding='utf-8') as f:
    long_description = f.read()
    print(long_description)
      
setup(
    name='mk-blender-scr',
    packages=find_packages(),
    install_requires=install_requirements, 
    version='1.0.3',
    author='Kato Taisetsu',
    url='https://shimi-lab.github.io/mk-blender-scr_Document/',
    description='Create a Python script for Blender from Atoms of ASE.',
    long_description=long_description,
    long_description_content_type='text/x-rst', # 'text/plain', 'text/x-rst', 'text/markdown'
    keywords='blender ase',
    entry_points={"console_scripts": ["mk-blender-scr = mk_blender_scr.command.cli:main"]},
)