from setuptools import find_packages, setup


NAME = 'pyraceview'
DESCRIPTION = 'Parse messages from NASCAR RaceView to extract race data'
URL = 'https://github.com/jdamiani27/pyraceview'
EMAIL = 'me@jasondamiani.com'
AUTHOR = 'Jason Damiani'
REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = [
    'numpy'
]

setup(
    name=NAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    license='MIT',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
