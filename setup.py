# Copyright 2020 NextThought
# Released under the terms of the LICENSE file.
import codecs
from setuptools import setup, find_packages


version = '0.0.1.dev0'

entry_points = {
}

TESTS_REQUIRE = [
    'coverage',
    'nti.testing',
    'zope.testrunner',
]

def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()

setup(
    name='nti.webhooks',
    version=version,
    author='Jason Madden',
    author_email='jason@nextthought.com',
    description="Python/Zope3 server-side webhooks implementation using ZODB and requests.",
    long_description=_read('README.rst') + '\n\n' + _read('CHANGES.rst'),
    license='Apache',
    keywords='webhook server event zope ZODB',
    url='https://github.com/NextThought/nti.webhooks',
    project_urls={
        'Documentation': 'https://ntiwebhooks.readthedocs.io/en/latest/',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope3',
        'Development Status :: 1 - Planning',
    ],
    zip_safe=False,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['nti'],
    install_requires=[
        'zope.interface >= 5.1',
        'zope.event',
        'setuptools',
        'transaction',
    ],
    entry_points=entry_points,
    include_package_data=True,
    extras_require={
        'test': TESTS_REQUIRE,
        'docs': [
            'Sphinx',
            'sphinx_rtd_theme',
            'repoze.sphinx.autointerface',
        ],
    },
)