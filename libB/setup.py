from setuptools import find_packages, setup

setup(
    name="lib_b",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "lib_a@git+ssh://git@github.com/ftnext/monorepo-python-practice@main"
        "#egg=lib_a&subdirectory=libA"
    ],
)
