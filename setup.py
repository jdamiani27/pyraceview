from setuptools import find_packages, setup


NAME = 'pyraceview'
DESCRIPTION = 'Parse messages from NASCAR RaceView to extract race data'
URL = 'https://github.com/jdamiani27/pyraceview'
EMAIL = 'me@jasondamiani.com'
AUTHOR = 'Jason Damiani'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.0.1'

REQUIRED = [
    'numpy'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    license='MIT',
)
