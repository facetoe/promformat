from setuptools import setup, find_packages

setup(
    name="promformat",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.9.3"
    ],
    tests_require=["pytest"],
    setup_requires=["flake8", "black"],
)
