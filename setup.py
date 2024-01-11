from setuptools import setup, find_packages

with open("README.md", "r",encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='floating_hippo',
    version='0.0.9',
    description='Floating Hippo is a simple, abstracted, and easy to use library for 2D simulations using Pymunk and Pygames.',
    long_description='Floating Hippo is a simple, abstracted, and easy to use library for 2D simulations using Pymunk and Pygames.',
    long_description_content_type='text/x-rst',
    author='Bijoy Kar',
    author_email='bjoykar54321@gmail.com',
    packages=find_packages(),
    license='MIT',
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

