from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

with open("README.rst") as f:
    long_description = f.read()

setup(name='clip-the-gym',
      version=version,
      description="Helper script to download audio from youtube for the gym",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Text Processing :: General',
      ],
      keywords='',
      author='Ralph Bean',
      author_email='rbean@redhat.com',
      url='http://github.com/ralphbean/clip-the-gym',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      [console_scripts]
      clip-the-gym = clipthegym:cmd
      """,
     )
