import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='legendary-camila-cruz',
    version='0.0.1',
    author='Camila Cruz',
    author_email='camilacruzdev@gmail.com',
    description='A subtitle delay corrector',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/camila-cruz/legendary',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)