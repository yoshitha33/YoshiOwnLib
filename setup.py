import setuptools

with open("README.md", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name ="YoshiOwnLib",
    version=0.1,
    author="Yoshitha Nunna",
    author_email="yoshithanunna77@gmail.com",
    description="A Python package for data analysis and visualization using Pandas, NumPy, Matplotlib, and Seaborn.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.0",
        "numpy>=1.18",
        "matplotlib>=3.0",
        "seaborn>=0.10"
    ],
)