import setuptools

setuptools.setup(
    name='xpathreader',
    version='1.0',
    packages=setuptools.find_packages() ,
    url='https://regmi-solutions.de/xpathreader',
    license='MIT',
    author='Bijay Regmi',
    author_email='bijay.regmi@uni-bonn.de',
    description='Reads xPath files. Documentation: https://regmi-solutions.de/xpathreader',
    python_requires = '>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
