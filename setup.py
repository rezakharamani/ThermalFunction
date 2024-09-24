from setuptools import setup, find_packages

setup(
    name='ThermalFunction',
    version='0.1.0',
    author='Reza Kharamani',
    author_email='rezakharamani@gmail.com',
    description='A simple Python library for basic math and string operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rezakharamani/ThermalFunction',  # Update with your actual GitHub repo
    packages=find_packages(),  # Automatically find all modules in the project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python version requirement
    install_requires=[],      # Add any external dependencies if required
)

