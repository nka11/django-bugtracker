import os
from setuptools import setup

import bugtracker

version = bugtracker.__version__
long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-bugtracker',
    version = version,
    packages = ['bugtracker'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A simple Django admin-based bug tracker app.',
    long_description = long_description,
    url = 'https://github.com/ahernp/django-bugtracker',
    author = 'Paul Ahern',
    author_email = 'ahernp@ahernp.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django==1.6.2',
    ],
)
