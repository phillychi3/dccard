import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dccard",
    version="0.1",
    author='phillychi3',
    author_email='phillychi3@gmail.com',
    description='a card generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phillychi3/dccard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",],
    packages = setuptools.find_packages(where="."),
    package_dir = {"":"."},
    python_requires=">=3.8",
)