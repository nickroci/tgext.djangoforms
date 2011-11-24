#!/usr/bin/env python
import setuptools
from distutils.core import setup

from sys import version
from setuptools import find_packages

if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
    
setup(name='tgext.djangoforms',
      install_requires=(
        'django',
        'TurboGears2 >= 2.1',
        'genshi'
        ),
        classifiers=[
          "Environment :: Web Environment",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: TurboGears"
          ],
        keywords='turbogears2.extension pylons',
        version='0.0.1',
        description='Allows you to use django forms with turbogears',
        author='Nick Holden',
        author_email='nickpholden@gmail.com',
        url='https://github.com/nickpholden/tgext.djangoforms',
        license='LGPL',
        packages=find_packages(exclude=['ez_setup']),
        namespace_packages=['tgext'],
        #scripts = ['path/to/script']
        )
