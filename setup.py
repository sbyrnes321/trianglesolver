from setuptools import setup

long_descrip = """
Written by Steven Byrnes, http://sjbyrnes.com/

Download: https://pypi.python.org/pypi/trianglesolver/
Source code repository: https://github.com/sbyrnes321/trianglesolver

This little package applies the law of sines or cosines to find all the
sides and angles of a triangle, if you know some of the sides and/or
angles.

The main function defined by this package is solve(...). Simple example::

    from math import pi
    from trianglesolver import solve
    a,b,c,A,B,C = solve(b=7.6, c=8.3, A=pi/3)

Following the usual convention, lower-case letters are side lengths and
capital letters are angles. Corresponding letters are opposite each other,
e.g. side b is opposite angle B.

All angles are in radians! However, you can use the degree constant to
convert::

    from trianglesolver import solve, degree
    a,b,c,A,B,C = solve(b=7, A=5*degree, B=70*degree)
    print(C / degree)
"""

descrip = ("Find all the sides and angles of a triangle, if you know some "
           "of the sides and/or angles. (Uses the Law of Sines and Law of "
           "Cosines.)")

setup(
    name = "trianglesolver",
    version = 1.1,
    author = "Steven Byrnes",
    author_email = "steven.byrnes@gmail.com",
    description = descrip,
    license = "MIT",
    keywords = "trigonometry, triangle, law of sines, law of cosines",
    url = "http://pypi.python.org/pypi/trianglesolver",
    py_modules=['trianglesolver'],
    long_description=long_descrip,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"]
)
