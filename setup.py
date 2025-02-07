from setuptools import setup, find_packages

setup(
    name="sisense-automl",
    version="0.1.7",
    description="A package for automating machine learning processes using Sisense and AutoML.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hnegi01/sisense-automl.git",
    author="Himanshu Negi",
    author_email="himanshu.negi.08@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'pandas==2.1.3',
        'numpy==1.23.5',
        'joblib==1.3.2',
        'scikit-learn==0.24.0',
        'auto-sklearn==0.15.0',
        'seaborn==0.13.2',
        'matplotlib==3.8.1',
        'Cython==3.0.11',
        'scipy==1.11.3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9, <3.10',
)
