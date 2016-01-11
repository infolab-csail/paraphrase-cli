from setuptools import setup

setup(
    name='paraphrase',
    version='0.1.0',
    description='A command-line wrapper to query textual entailment '
                'and paraphrasing systems',
    author='Alvaro Morales',
    author_email='alvarom@csail.mit.edu',
    url='https://github.com/infolab-csail/paraphrase-cli.git',
    packages=[
        'paraphrase'
    ],
    install_requires=[
        'lxml',
        'requests',
    ],
    tests_require=[
        'nose>=1.0',
    ],
    entry_points={
        'console_scripts': [
            'excitement = paraphrase.cli:main',
        ],
    },
    test_suite='nose.collector',
)
