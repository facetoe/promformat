from setuptools import setup, find_packages

setup(
    name="promformat",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.10"
    ],
    tests_require=["pytest"],
    setup_requires=["flake8", "black"],
    entry_points = {
        'console_scripts': [
            'promformat = promformat.__main__:main',
        ],
    },
)
