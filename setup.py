import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="populi-mrobison",
    version="0.0.2",
    author="Mike Robison",
    author_email="mrobison@wts.edu",
    description="A module for interacting with the populi api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/populi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['lxml', 'pycurl'],
)

#from distutils.core import setup

# To use locally: pip install -e ../populi-api-python/

#setup(name='populi',
#    version='1.0',
#    py_modules=['populi'],
#    install_requires=[
#        'lxml',
#        'pycurl'
#    ]
#)