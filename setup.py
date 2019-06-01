from setuptools import setup, find_packages

setup(
    name="ikea-smartlight",
    version="2.0.0",
    scripts=["./traadfri"],
    install_requires=["docopt", "schema", "ansicolors"],
    packages=find_packages(),
)
