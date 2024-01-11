from setuptools import setup, find_packages

setup(
    name='floating_hippo',
    version='0.0.9',
    description='Floating Hippo is a simple, abstracted, and easy to use library for 2D simulations using Pymunk and Pygames.',
    long_description=open('README.md').read(),
    author='Bijoy Kar',
    author_email='bjoykar54321@gmail.com',
    packages=find_packages(),
    install_requires=['pygame','pymunk'],
    keywords=['physics','simulation','pymunk','pygame'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

