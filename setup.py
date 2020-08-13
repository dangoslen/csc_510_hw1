
from setuptools import setup, find_packages

setup(
    name='csc_510_hw1',
    version='0.1',
    description='Learning how to build a cool github repo', 
    author='Harsh Kachhadia',
    author_email='hmkachha@ncsu.edu',
    url='https://github.com/dangoslen/csc_510_hw1',
    packages=find_packages(include=['code', 'code.*','data']),
    long_description="""Learning how to build a cool github repo""",
    classifiers=[
          "License :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: cool github repo",
      ],
    keywords='csc-510 hw1 csc-510-hw1',
    license='MIT License',	
    install_requires=['numpy'], #numpy is just for sample
    tests_require=['pytest'],
    package_data={'data':['sample_data.json']}
)

