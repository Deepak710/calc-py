import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='Calculator',
    version='0.1a1.dev1',
    author='Deepak Balaji',
    author_email='deepakb.messi@gmail.com',
    description='A Simple Calculator Program to showcase basic python operations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deepak710/calc-py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: GNU GPLv3 :: Self Approved(DMB710)",
        "Operating System :: OS Independent",
    ),
)
