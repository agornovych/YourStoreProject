from setuptools import setup, find_packages


def get_dependencies():
    deps = None
    with open("dependencies.txt", "r") as deps:
        deps = tuple(map(lambda dep: dep.strip(), deps.readlines()))

    return deps


setup(
    name="Store Project Testing Framework",
    version="1.0.0",
    author="Alex Hornovych",
    author_email="a.gornovych@gmail.com",
    packages=find_packages(),
    install_requires=get_dependencies()
)