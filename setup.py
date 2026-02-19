from setuptools import setup, find_packages

setup(
    name="promformat",
    version="1.0.2",
    packages=find_packages(exclude=["tests*"]),
    install_requires=["antlr4-python3-runtime>=4.10"],
    tests_require=["pytest", "PyYAML", "setuptools"],
    setup_requires=["flake8", "black", "setuptools"],
    entry_points={
        "console_scripts": [
            "promformat = promformat.__main__:main",
        ],
    },
)
