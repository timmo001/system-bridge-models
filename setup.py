"""Setup."""
from setuptools import find_packages, setup

# Get setup packages from requirements.txt
with open("requirements_setup.txt", encoding="utf-8") as f:
    requirements_setup = f.read().splitlines()

# Get packages from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="systembridgemodels",
    author="Aidan Timson (Timmo)",
    author_email="aidan@timmo.dev",
    description="System Bridge Models",
    keywords="system-bridge",
    license="Apache-2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/timmo001/system-bridge-models",
    install_requires=requirements,
    packages=find_packages(exclude=["tests", "tests.*", "generator"]),
    python_requires=">=3.11",
    setup_requires=requirements_setup,
    use_incremental=True,
)
