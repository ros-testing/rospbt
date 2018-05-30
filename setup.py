from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name = 'rostestplus',
    version = '0.1.0',
    packages = find_packages(),
    install_requires=install_requires,
)

