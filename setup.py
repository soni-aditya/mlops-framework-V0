from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    description="its a wine Q package",
    author="soni-aditya",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        'mamba',
        'dvc',
        'dvc-gdrive',
        'scikit-learn',
        'pandas',
        'pytest',
        'tox',
        'flake8',
        'flask',
        'gunicorn',
        'PyYAML',
        'joblib==1.2.0'
    ]
)
