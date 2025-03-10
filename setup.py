import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, "README.md"), "r") as f:
    long_description = f.read()

setup(
    name="logging_json",
    version=open("logging_json/version.py").readlines()[-1].split()[-1].strip("\"'"),
    author="Colin Bounouar",
    author_email="colin.bounouar.dev@gmail.com",
    maintainer="Colin Bounouar",
    maintainer_email="colin.bounouar.dev@gmail.com",
    url="https://colin-b.github.io/logging_json/",
    description="JSON formatter for python logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://pypi.org/project/logging_json/",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords=["logging", "json"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    extras_require={
        "testing": [
            # Used to check coverage
            "pytest-cov==4.*",
        ]
    },
    python_requires=">=3.7",
    project_urls={
        "GitHub": "https://github.com/Colin-b/logging_json",
        "Changelog": "https://github.com/Colin-b/logging_json/blob/master/CHANGELOG.md",
        "Issues": "https://github.com/Colin-b/logging_json/issues",
    },
    platforms=["Windows", "Linux"],
)
