from __future__ import absolute_import
from setuptools import setup, find_packages
from setuptools.command.install import install


class InstallCommand(install):
    user_options = install.user_options + [
        ('no-ml', None, "Don't install without Machine Learning modules."),
    ]

    boolean_options = install.boolean_options + ['no-ml']

    def initialize_options(self):
        install.initialize_options(self)

    def finalize_options(self):
        install.finalize_options(self)
        dist = self.distribution
        dist.packages=find_packages(exclude=[
            'tests',
            'tests.*',
            'talon.signature',
            'talon.signature.*',
        ])


setup(name='talon',
      version='1.4.8',
      description=("Mailgun library "
                   "to extract message quotations and signatures."),
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='https://github.com/mailgun/talon',
      license='APACHE2',
      cmdclass={
          'install': InstallCommand,
      },
      packages=find_packages(exclude=['tests', 'tests.*']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "lxml>=2.3.3",
          "regex==2021.11.10",
          'chardet>=1.0.1',
          'cchardet>=0.3.5',
          'cssselect',
          'six>=1.10.0',
          'html5lib'
          ],
      tests_require=[
          "mock",
          "nose>=1.2.1",
          "coverage"
          ]
      )
