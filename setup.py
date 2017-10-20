"""Setup, requirements, info for Mailroom project"""

from setuptools import setup

setup(
    name='mailroom',
    description='Commandline tool to send donor emails and create reports',
    author='Chelsea Dole, Kinley Ramson',
    author_email='chelseadole@gmail',
    package_dir={' ': 'src'},
    py_modules=['ackermann'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']},
    entry_points={
        'console_scripts': [
            'mailroom = mailroom:initial_prompt']
    }
)
