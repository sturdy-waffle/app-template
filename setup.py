import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


with open("sturdy_waffle/_version.py", "r", encoding="utf-8") as fh:
    exec(fh.read())


setuptools.setup(
    name="sturdy_waffle",
    version=__version__,
    author="Sturdy Waffle Inc",
    author_email="support@sturdywaffle.com",
    description="Sturdy waffle applicance",
    license="Proprietary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sturdywaffle.com",
    packages=setuptools.find_packages(include=["sturdy_waffle"]),
    package_data={"sturdy_waffle": ["sturdy_waffle/templates/*", "sturdy_waffle/static/*"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "Flask>=1.1.0",
        "gunicorn>=20.00",
    ]
)
