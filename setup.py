from setuptools import setup


setup(
    name='nepali-unicode-converter',
    version='1.0.1',
    description='Roman text to unicode converter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bibek Pandey',
    author_email='bewakepandey@gmail.com',
    url='https://github.com/bewakes/nepali-unicode-converter',
    package_data={'': ['word_maps.txt']},
    packages=['nepali_unicode_converter'],
 )
