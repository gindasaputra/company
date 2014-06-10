from distutils.core import setup

setup(name='company',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Reconcile company names with OpenCorporates.',
      url='https://github.com/tlevine/company',
      packages=['company'],
      install_requires = [
          'pickle_warehouse >= 0.0.18',
          'requests>=2.2.1',
      ],
      scripts = [
      ],
      tests_require = ['nose'],
      version='0.0.1',
      license='AGPL',
      classifiers=[
          'Programming Language :: Python :: 3.4',
      ],
)
