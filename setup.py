from setuptools import setup, find_packages

setup(
    name="ikea-smartlight",
    version="0.1.0",
    scripts=["./traadfri"],
    install_requires=["docopt", "schema", "ansicolors"],
    packages=find_packages(),
)
