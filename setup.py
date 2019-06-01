from setuptools import setup, find_packages

setup(
    name="ikea-smartlight",
    version="2.0.0",
    scripts=["./traadfri"],
    install_requires=["docopt", "schema", "ansicolors"],
    packages=["traadfrilib"],
    test_suite="traadfrilib.tests",
)
