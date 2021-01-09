from setuptools import setup, find_packages


long_description = '''# Internet Explorer API
Python package for Windows<br />
[GitHub](https://github.com/Pixelsuft/iexplorer-api)<br />
![Screenshot](https://github.com/Pixelsuft/iexplorer-api/blob/main/iexplorer.png?raw=true)'''

setup(
    name="iexplorer_api",
    version="0.0.1",
    author="Pixelsuft",
    description="Internet Explorer API written on C++ Builder 6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/small_win_tools/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT', 
    keywords='iexplorer_api',
    install_requires=[''],
    py_modules=["iexplorer_api","urllib"]
)