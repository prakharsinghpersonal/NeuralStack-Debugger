from setuptools import setup, find_packages

setup(
    name="neural_stack_debugger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "ns-visualize=tools.visualize:main",
        ],
    },
    author="Prakhar Singh",
    description="Tooling for AI inference training, evaluation, and benchmarking.",
)
