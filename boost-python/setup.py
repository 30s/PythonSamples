#!/usr/bin/env python
 
from distutils.core import setup
from distutils.extension import Extension
 
setup(name="hello",
    ext_modules=[
        Extension("hello", ["hello.cpp"],
        libraries = ["boost_python"])
    ])
