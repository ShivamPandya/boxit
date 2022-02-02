from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'A CLI utility to make your text stand out'
LONG_DESCRIPTION = 'This package allows you to put important titles in box. You get to pick colors too!'

setup(
        name="boxit",
        url='https://github.com/shivampandya/boxit',
        version=VERSION,
        author="Shivam Pandya",
        author_email="shivamnyt@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        py_modules=['boxit'],
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'boxit', 'text color', 'tabular', 'ascii', 'box'],
        classifiers= [
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)