from re import search
from setuptools import setup, find_packages


with open("README.md", "r") as stream:
    long_description = stream.read()
    
with open(f'json_file/__init__.py') as fp:
    __version__ = search("'" + (r"\d*." * 5) + "'", 
                         fp.read()).group().replace("'", '')

setup(
    name="json_file",
    version=__version__,
    url="https://github.com/Alert-Aigul/JsonFile",
    download_url="https://github.com/Alert-Aigul/JsonFile/archive/refs/heads/main.zip",
    license="MIT",
    author="Alert Aigul",
    author_email="alertaigul@gmail.com",
    description="Dict as json file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "jsonfile",
        "json",
        "file",
        "dict",
        "python",
        "python3",
        "python3.x",
        "alertaigul",
        "tool"
    ],
    install_requires=[
        "setuptools",
        "aiofiles"
    ],
    setup_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    packages=find_packages()
)