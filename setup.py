from setuptools import setup, find_packages
import glob
import os
import pkg_resources

from squirrel import __version__, _program

setup(name='squirrel',
      version=__version__,
      packages=find_packages(),
      scripts=[
            'squirrel/scripts/msa.smk',
            'squirrel/scripts/reconstruction.smk'
                ],
      package_data={"squirrel":["data/*"]},
      install_requires=[
            "biopython>=1.70",
            'tabulate==0.8.10',
            'baltic',
            'matplotlib',
            'seaborn',
            'pandas'
        ],
      description='Some QUIck Rearranging to Resolve Evolutionary Links',
      url='https://github.com/cov-lineages/squirrel',
      author='Aine OToole',
      author_email='aine.otoole@ed.ac.uk',
      entry_points="""
      [console_scripts]
      {program} = squirrel.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)
