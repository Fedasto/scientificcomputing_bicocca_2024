from setuptools import setup, find_packages

setup(name='montecarloSimulation',
      description='exercise8',
      author='Federico Astori',
      license='MIT',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib', 'numba'])