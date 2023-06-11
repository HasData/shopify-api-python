import os

from setuptools import setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'shopify_api', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name='shopify-python-api',
    version=about['__version__'],
    url='https://github.com/Scrapeit-Cloud/shopify-api-python',
    description='Real-Time Shopify API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Roman Milyushkevich',
    author_email='roman@scrape-it.cloud',
    maintainer='Roman Milyushkevich',
    maintainer_email='roman@scrape-it.cloud',
    license='MIT',
    packages=['shopify_api'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)
