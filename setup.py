from setuptools import setup, find_packages

setup(
    name='dv',
    version='1.0.0',
    author='Raghav Singhal',
    author_email='singhalraghav.59@gmail.com',
    description='A package for data visualization',
    long_description='A package that provides functionality for data visualization using pandas, seaborn, and matplotlib.',
    long_description_content_type='text/markdown',
    url='https://github.com/raghav29061999/dv',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
