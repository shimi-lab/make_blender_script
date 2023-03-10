from setuptools import setup, find_packages

console_scripts = [
]

long_description = """
====================================================
化学構造をBlender上で作成するためのライブラリ
====================================================

| cif,xyz,VASPの構造ファイルをBeldnerに取り込むためのライブラリ
| Blender上で動作するPythonスクリプトを生成する.


ドキュメント
-------------------------

https://shimi-lab.github.io/mk-blender-scr_Document/


インポート可能な構造ファイル
------------------------------

| ASEのAtomsオブジェクトを作成する必要があるため,VASP(POSCAR,CONTCAR), xyz, cif等を読み込むことができる.
| 詳細なフォーマットは以下を参照
| https://wiki.fysik.dtu.dk/ase/ase/io/io.html

Pythonバージョン
------------------

Python3.8,Python3.10での動作確認済

依存ライブラリ
----------------

| 以下の条件下で安定的な動作が確認されている.
| nglview==3.0.3の場合,ipywidgetsは8.0以下である必要があることが知られている.

- `ase==3.22.1 <https://wiki.fysik.dtu.dk/ase/>`_
- `Jinja2==3.1.2 <https://jinja.palletsprojects.com/en/3.1.x/>`_
- `ipywidgets==7.7.2 <https://ipywidgets.readthedocs.io/en/stable/index.html>`_
- `nglview==3.0.3 <https://pypi.org/project/nglview/>`_

Blenderバージョン
--------------------
Blender2.9, Blender3.0 での動作確認済

"""

setup(
    name='mk-blender-scr',
    packages=find_packages(),
    install_requires=['ase', 'nglview', 'jinja2','ipywidgets'], 
    version='1.0.1',
    author='Kato Taisetsu',
    url='https://shimi-lab.github.io/mk-blender-scr_Document/',
    description='Create a Python script for Blender from Atoms of ASE.',
    long_description=long_description,
    long_description_content_type='text/x-rst', # 'text/plain', 'text/x-rst', 'text/markdown'
    keywords='blender ase',
    entry_points={'console_scripts': console_scripts},
)