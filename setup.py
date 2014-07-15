from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tostadaspipo',
      version=version,
      description="Ejemplos de conjuntos de Tostadas a que pipo",
      long_description="""\
Ejemplos de conjuntos de Tostadas a que pipo, para demostrar como creat un paquete Egg Python.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conujtos tostadas pipo',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/Covantec/tostadaspipo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
