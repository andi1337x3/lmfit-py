from setuptools import setup, find_packages
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """
    TODO: Sense of this redefinition? - Max 09.10.18
    """
    def is_pure(self):
        """
        TODO: Sense of this redefinition? - Max 09.10.18
        """
        return False
#  Tutorials:
#       http://www.ewencp.org/blog/a-brief-introduction-to-packaging-python/
#       https://pythonhosted.org/setuptools/setuptools.html#using-find-packages
#       http://stackoverflow.com/questions/4740473/setup-py-examples
#       https://docs.python.org/2/distutils/setupscript.html
#       https://docs.python.org/3.4/distutils/builtdist.html
#       http://lucumr.pocoo.org/2014/1/27/python-on-wheels/


# Define excluded packages:
EXCLUDED_PACKAGES = []

setup(name='lmfit',
      version="0.0.1", # modified by araab
      #use_scm_version={
      #    'write_to': 'lmfit/version.py',
      #    'version_scheme': 'post-release'},
      author='LMFit Development Team',
      author_email='matt.newville@gmail.com',
      url='https://lmfit.github.io/lmfit-py/',
      download_url='https://lmfit.github.io//lmfit-py/',
      setup_requires=['setuptools_scm'],
      install_requires=['asteval>=0.9.22',
                        'numpy>=1.18',
                        'scipy>=1.3',
                        'uncertainties>=3.0.1'],
      python_requires='>=3.6',
      license='BSD-3',
      description="Least-Squares Minimization with Bounds and Constraints",
      #long_description=long_desc,
      platforms=['Windows', 'Linux', 'Mac OS X'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Topic :: Scientific/Engineering',
                   ],
      keywords='curve-fitting, least-squares minimization',
      tests_require=['pytest'],
      package_dir={'lmfit': 'lmfit'},
      packages=['lmfit'],
      )
