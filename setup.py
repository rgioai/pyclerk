import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclerk",
    version="0.0.1",
    author="Ryan Giarusso",
    author_email="rgiarusso@jd20.law.harvard.edu",
    description="Use python to access all U.S. caselaw through the Harvard Law School Library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rgioai/caselaw-access-project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.6'
)
