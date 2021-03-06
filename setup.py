#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------

from setuptools import setup
from django_mailer import get_version

setup(
    name='django-mailer-2',
    version=get_version(),
    description=("A reusable Django app for queueing the sending of email "
                 "(forked of APSL/django-mailer-2, which is unmaintained)"),
    long_description=open('docs/usage.rst').read(),
    author='Maykin Media',
    author_email='info@maykinmedia.nl',
    url='https://github.com/maykinmedia/django-mailer-2',
    install_requires=["pyzmail", ],
    packages=[
        'django_mailer',
        'django_mailer.management',
        'django_mailer.management.commands',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
