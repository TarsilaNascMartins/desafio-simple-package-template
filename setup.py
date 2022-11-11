# from setuptools import setup, find_packages

# with open("README.md", "r") as f:
#     page_description = f.read()

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

# setup(
#     name="package_aumentosalario",
#     version="0.0.1",
#     author="Tarsila Martins",
#     author_email="tarsilawho@gmail.com",
#     description="My short description",
#     long_description=page_description,
#     long_description_content_type="text/markdown",
#     url='https://github.com/TarsilaNascMartins/desafio-simple-package-template',
#     packages=find_packages(),
#     install_requires=requirements,
#     python_requires='>=3.8',
   
# )

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libradocs", # Replace with your own username
    version="0.0.0",
    author="Tarsila Nascimento",
    author_email="tarsilawho@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    homepage="https://github.com/TarsilaNascMartins/desafio-simple-package-template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)