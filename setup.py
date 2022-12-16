from setuptools import setup

setup(
    name="promformat",
    version="0.0.4",
    packages=["promformat"],
    install_requires=["antlr4-python3-runtime>=4.10"],
    tests_require=["pytest"],
    setup_requires=["flake8", "black"],
    entry_points={
        "console_scripts": [
            "promformat = promformat.__main__:main",
        ],
    },
)
