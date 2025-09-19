"""Setup."""
from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="systembridgemodels",
    version="4.2.6",
    author="Aidan Timson (Timmo)",
    author_email="aidan@timmo.dev",
    description="System Bridge Models",
    keywords="system-bridge",
    license="Apache-2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/timmo001/system-bridge-models",
    packages=find_packages(exclude=["tests", "tests.*", "generator"]),
    python_requires=">=3.11",
)
