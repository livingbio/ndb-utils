import os


from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


REQUIREMENTS = [
    'django',
    'pyyaml',
    'Pillow',
    'coverage',
    'unittest2',
    'nose',
    'gcloud',
]

setup(
    name='ndb-utils',
    version='0.0.1',
    description='ndb utils',
    author='lucemia',
    author_email='lucemia@gmail.com',
    long_description=README,
    scripts=[],
    url='https://github.com/lucemia/gcloud-python-orm',
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
