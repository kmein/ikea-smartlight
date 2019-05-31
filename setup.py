from setuptools import setup, find_packages

setup(
    name="ikea-smartlight",
    version="0.1.0",
    scripts=["./tradfri-groups.py", "./tradfri-lights.py", "./tradfri-status.py"],
    install_requires=["tqdm"],
    packages=find_packages()
)
