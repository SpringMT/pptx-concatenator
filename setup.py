from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pptx-concatenator",
    version="0.1.0",
    description="PowerPoint concatenation library using pptx-slide-copier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Makoto Haruyama",
    author_email="",
    url="https://github.com/makoto/pptx-concatinator",
    project_urls={
        "Bug Tracker": "https://github.com/makoto/pptx-concatinator/issues",
        "Source Code": "https://github.com/makoto/pptx-concatinator",
    },
    py_modules=["pptx_concat"],
    install_requires=requirements,
    python_requires=">=3.6",
    keywords=["powerpoint", "pptx", "concatenate", "merge", "presentation"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
