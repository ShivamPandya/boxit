from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'A CLI utility to make your text stand out'
LONG_DESCRIPTION = 'This package allows you to put important titles in box. You get to pick colors too!'

setup(
        name="boxit",
        url='https://github.com/shivampandya/boxit',
        version=VERSION,
        author="Shivam Pandya",
        author_email="sampandyasp@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        py_modules=['boxit'],
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'boxit', 'text color', 'tabular', 'ascii', 'box'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)