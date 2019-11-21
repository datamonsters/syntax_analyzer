from setuptools import find_packages, setup

setup(
    name='syntax-analyzer',
    version='0.1',
    description='Syntax Analyzer',
    url='https://github.com/datamonsters/syntax_analyzer',
    author='Data Monsters',
    author_email='support@datamonsters.co',
    packages=find_packages(),
    package_data={
        'syntax_analyzer': ['dict/*'],
    },
    include_package_data=True,
    python_requires='>=3.6'
)
