from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyky040',
    version='0.1.5',
    description='High-level interface for the KY040 rotary encoder and switch.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/azazelcodes/pyKY040',
    author='Azazel',
    author_email='azazel.codes@gmail.com',
    keywords='keyes rotary encoder switch ky040',
    #py_modules=["pyky040"],
    packages=find_packages(),
    install_requires=['RPi.GPIO'],
    extras_require={
        "device": ["evdev"]
    },
)
