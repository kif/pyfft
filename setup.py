try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

from test.doc import DOCUMENTATION

VERSION = '0.2'

# generate .rst file with documentation
open(os.path.join(os.path.dirname(__file__), 'documentation.rst'), 'w').write(DOCUMENTATION)

setup(
	name='pyfft',
	packages=['pyfft'],
	requires=['mako', 'numpy'],
	version=VERSION,
	author='Bogdan Opanchuk',
	author_email='mantihor@gmail.com',
	url='http://github.com/Manticore/pyfft',
	description='FFT library for PyCuda and PyOpenCL',
	long_description=DOCUMENTATION,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Topic :: Scientific/Engineering :: Mathematics'
	]
)
