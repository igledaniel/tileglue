from setuptools import setup, find_packages

version = '0.0.1.dev'

setup(name='tileglue',
      version=version,
      description=("Glue together tile packages and house mapzen "
                   "specific details"),
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'redis',
          'tilequeue',
          'tilestache-providers',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
